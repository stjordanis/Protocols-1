from opentrons import labware, instruments, modules
import math

metadata = {
    'protocolName': 'Sample Aliquoting',
    'author': 'Nick <protocols@opentrons.com>',
    'source': 'Custom Protocol Request'
}

# create custom labware
source_name = 'GE-96-collection'
if source_name not in labware.list():
    labware.create(
        source_name,
        grid=(12, 8),
        spacing=(9, 9),
        diameter=6,
        depth=28,
        volume=500
    )

dest_name = 'Micronic-96-1-rack'
if dest_name not in labware.list():
    labware.create(
        dest_name,
        grid=(12, 8),
        spacing=(9, 9),
        diameter=7,
        depth=17,
        volume=50
    )

# load labware
tips300 = labware.load('opentrons-tiprack-300ul', '3')
tips50 = labware.load('opentrons-tiprack-300ul', '6')

# pipettes
m300 = instruments.P300_Multi(mount='right', tip_racks=[tips300])
p50 = instruments.P50_Single(mount='left', tip_racks=[tips50])


def run_custom_protocol(
        tempdeck_temperature_in_degrees_C: float = 4,
        number_of_protein_samples: int = 48
):
    # checks
    if number_of_protein_samples > 48 or number_of_protein_samples < 1:
        raise Exception('Invalid number of protein samples.')

    # load tempdeck and plate
    tempdeck = modules.load('tempdeck', '1')
    source_plate = labware.load(source_name, '1', share=True)
    tempdeck.set_temperature(tempdeck_temperature_in_degrees_C)
    tempdeck.wait_for_temp()

    # consolidate protein samples
    num_cons = math.ceil(number_of_protein_samples/8)
    sources = [source_plate.rows('A')[i*2+1] for i in range(num_cons)]
    cons_locs = [source_plate.rows('A')[i*2] for i in range(num_cons)]
    for s, d in zip(sources, cons_locs):
        m300.pick_up_tip()
        m300.transfer(100, s, d, new_tip='never')
        m300.mix(5, 150, d)
        m300.blow_out(d.top())
        m300.drop_tip()

    # destination plate setup
    num_dests = number_of_protein_samples*8
    num_dest_racks = math.ceil(num_dests/96)
    dest_locs = ['4', '5', '7', '8'][:num_dest_racks]
    dest_racks = [
        labware.load(dest_name, slot, 'destination rack ' + str(i+1))
        for i, slot in enumerate(dest_locs)
    ]
    dest_cols = [col for rack in dest_racks
                 for col in rack.columns()][:number_of_protein_samples]
    rep_dests = [[well for well in col] for col in dest_cols]
    rep_sources = [
        well for loc in cons_locs
        for well in source_plate.wells(loc.get_name(), length=8)
    ]

    # transfer aliquots
    for s, d in zip(rep_sources, rep_dests):
        p50.distribute(
            25,
            s,
            [well.top() for well in d],
            disposal_vol=0,
        )
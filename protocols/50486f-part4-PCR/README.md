# PCR Prep 4/4: PCR

### Author
[Opentrons](https://opentrons.com/)

## Categories
* Sample Prep
	* PCR


## Description
This protocol performs PCR prep - PCR (part 4/4) for 96 samples using the P10 Multi-channel pipette.

---
![Materials Needed](https://s3.amazonaws.com/opentrons-protocol-library-website/custom-README-images/001-General+Headings/materials.png)

* [P10 Multi-channel Pipette](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette)
* [10uL Opentrons tipracks](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-10ul-tips)
* [Bio-Rad 96-Well PCR Plate](https://labware.opentrons.com/biorad_96_wellplate_200ul_pcr?category=wellPlate)
* [Labcon 0.2mL PCR Strips](http://www.labcon.com/microstrips.html)
* [Labcon 96-Well PCR Plate](http://www.labcon.com/micro.html)
* PCR Cooler


---
![Setup](https://s3.amazonaws.com/opentrons-protocol-library-website/custom-README-images/001-General+Headings/Setup.png)

Slot 1: Labcon PCR Plate on PCR Cooler (clean and empty)

Slot 2: Labcon 0.2mL PCR Strip on PCR Cooler (Column 1)

Slot 3: Bio-Rad PCR plate, filled with primers.

Slot 4: Labcon PCR Plate on 96-well Aluminum Block (with samples from Step 3 - EXO)

Slot 5-11: [10uL Opentrons tipracks](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-10ul-tips)

### Robot
* [OT-2](https://opentrons.com/ot-2)

## Process

1. Input your protocol parameters.
2. Download your protocol.
3. Upload your protocol into the [OT App](https://opentrons.com/ot-app).
4. Set up your deck according to the deck map.
5. Calibrate your labware, tiprack and pipette using the OT App. For calibration tips, check out our [support articles](https://support.opentrons.com/en/collections/1559720-guide-for-getting-started-with-the-ot-2).
6. Hit "Run".

### Additional Notes
This protocol is designed for preparing a 96-well sample and for use with the P10 Multi-channel pipette.

If you have any questions about this protocol, please contact the Protocol Development Team by filling out the [Troubleshooting Survey](https://protocol-troubleshooting.paperform.co/).

###### Internal
50486f
# PsychoPy triggers for BioSemi ActiveTwo

This is a minimal example of how to send triggers from PsychoPy to a BioSemi ActiveTwo system, using a BioSemi provided trigger interface. It implements a basic oddball paradigm with auditory stimuli (standards at 500 Hz,  deviants at 800 Hz). The sounds are generated as sine waves using the PsychoPy backend. Everything works as of PsychoPy v. 2023.2.3. Before you use the paradigm, make sure that you:

- Figure out the identifier that your OS uses for the serial port / USB emulator and put it in `serial_port_address`
- Make sure everything is connected (the script will bug out without a working serial port). If you want to test without the EEG system, comment out all lines that utilize the `port` object.

More info on identifiers: <https://workshops.psychopy.org/3days/day3/hardware/index.html>

Kudos to Aniela Brzezińska and Bartosz Witkowski for coding.

<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 1-bit full adder.

- `ui_in[0]` is operand A
- `ui_in[1]` is operand B
- `ui_in[2]` is carry-in
- `uo_out[0]` is the sum bit
- `uo_out[1]` is the carry-out bit

The remaining input and output pins are tied off because the design does not use them.

## How to test

Drive the three least-significant input bits with all 8 combinations and check the two least-significant output bits against the full-adder truth table.

For local simulation, run the cocotb test in `test/`.

## External hardware

No external hardware is required.

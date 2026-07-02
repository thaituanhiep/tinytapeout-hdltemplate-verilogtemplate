# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Exercise the 1-bit full-adder truth table on ui_in[2:0].
    vectors = [
        (0b000, 0b00),
        (0b001, 0b01),
        (0b010, 0b01),
        (0b011, 0b10),
        (0b100, 0b01),
        (0b101, 0b10),
        (0b110, 0b10),
        (0b111, 0b11),
    ]

    for inputs, expected in vectors:
        dut.ui_in.value = inputs
        dut.uio_in.value = 0
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == expected

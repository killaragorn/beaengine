#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *


class TestSuite:
    def test(self):

        # VEX.NDS.128.66.0F38.W0 ac /r
        # vfnmadd213ps xmm1, xmm2, xmm3/m128
        Buffer = 'c40201ac443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfnmadd213ps ')
        assert_equal(myDisasm.instr.repr, 'vfnmadd213ps xmm8, xmm15, xmmword ptr [r11+r14+22h]')

        # VEX.NDS.256.66.0F38.W0 ac /r
        # vfnmadd213ps ymm1, ymm2, ymm3/m256
        Buffer = 'c40205ac443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfnmadd213ps ')
        assert_equal(myDisasm.instr.repr, 'vfnmadd213ps ymm8, ymm15, ymmword ptr [r11+r14+22h]')

        # EVEX.NDS.128.66.0F38.W0 ac /r
        # vfnmadd213ps xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '62020506ac443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xac')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfnmadd213ps ')
        assert_equal(myDisasm.instr.repr, 'vfnmadd213ps xmm0, xmm15, xmmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.256.66.0F38.W0 ac /r
        # vfnmadd213ps ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '62020520ac443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xac')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfnmadd213ps ')
        assert_equal(myDisasm.instr.repr, 'vfnmadd213ps ymm0, ymm15, ymmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.512.66.0F38.W0 ac /r
        # vfnmadd213ps zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '62020540ac443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xac')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfnmadd213ps ')
        assert_equal(myDisasm.instr.repr, 'vfnmadd213ps zmm0, zmm15, zmmword ptr [rbx+rsi+22h]')


        # VEX.NDS.128.66.0F38.W1 ac /r
        # vfnmadd213pd xmm1, xmm2, xmm3/m128

        myVEX = VEX()
        myVEX.L = 0
        myVEX.W = 1
        myVEX.pp = 0b1
        myVEX.mmmm = 0b10
        myVEX.vvvv = 0b0

        Buffer = 'c4{:02x}{:02x}ac443322'.format(myVEX.byte1(), myVEX.byte2()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfnmadd213pd ')
        assert_equal(myDisasm.instr.repr, 'vfnmadd213pd xmm8, xmm15, xmmword ptr [r11+r14+22h]')

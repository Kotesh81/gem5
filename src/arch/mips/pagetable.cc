/*
 * Copyright (c) 2002-2005 The Regents of The University of Michigan
 * Copyright (c) 2007 MIPS Technologies, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met: redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer;
 * redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution;
 * neither the name of the copyright holders nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include "arch/mips/pagetable.hh"

#include "sim/serialize.hh"

namespace gem5
{

namespace MipsISA
{

void
PTE::serialize(CheckpointOut &cp) const
{
    SERIALIZE_SCALAR(Mask);
    SERIALIZE_SCALAR(VPN);
    SERIALIZE_SCALAR(asid);
    SERIALIZE_SCALAR(G);
    SERIALIZE_SCALAR(PFN0);
    SERIALIZE_SCALAR(D0);
    SERIALIZE_SCALAR(V0);
    SERIALIZE_SCALAR(C0);
    SERIALIZE_SCALAR(PFN1);
    SERIALIZE_SCALAR(D1);
    SERIALIZE_SCALAR(V1);
    SERIALIZE_SCALAR(C1);
    SERIALIZE_SCALAR(AddrShiftAmount);
    SERIALIZE_SCALAR(OffsetMask);
}

void
PTE::unserialize(CheckpointIn &cp)
{
    UNSERIALIZE_SCALAR(Mask);
    UNSERIALIZE_SCALAR(VPN);
    UNSERIALIZE_SCALAR(asid);
    UNSERIALIZE_SCALAR(G);
    UNSERIALIZE_SCALAR(PFN0);
    UNSERIALIZE_SCALAR(D0);
    UNSERIALIZE_SCALAR(V0);
    UNSERIALIZE_SCALAR(C0);
    UNSERIALIZE_SCALAR(PFN1);
    UNSERIALIZE_SCALAR(D1);
    UNSERIALIZE_SCALAR(V1);
    UNSERIALIZE_SCALAR(C1);
    UNSERIALIZE_SCALAR(AddrShiftAmount);
    UNSERIALIZE_SCALAR(OffsetMask);
}

} // namespace MipsISA
} // namespace gem5

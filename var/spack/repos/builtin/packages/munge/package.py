# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Munge(AutotoolsPackage):
    """ MUNGE Uid 'N' Gid Emporium """
    homepage = "https://code.google.com/p/munge/"
    url      = "https://github.com/dun/munge/releases/download/munge-0.5.13/munge-0.5.13.tar.xz"
    version('0.5.13', sha256='99753dfd06a4f063c36f3fb0eb1964f394feb649937d94c4734d85b7964144da')
    version('0.5.12', sha256='e972e3c3e947995a99e023f5758047db16cfe2f0c2c9ca76399dc1511fa71be8')
    version('0.5.11', sha256='8e075614f81cb0a6df21a0aafdc825498611a04429d0876f074fc828739351a5',
            url='https://github.com/dun/munge/releases/download/munge-0.5.11/munge-0.5.11.tar.bz2')

    depends_on('openssl')
    depends_on('libgcrypt')

    def install(self, spec, prefix):
        os.makedirs(os.path.join(prefix, "lib/systemd/system"))
        super(Munge, self).install(spec, prefix)

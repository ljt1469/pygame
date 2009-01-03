# This file is generated with mmp2sconscript
from scons_symbian import *

target     = "vorbis"
targettype = "lib"
libraries  = []
# Static libs
libraries += []


uid3 = 0



sources = ['deps/vorbis/lib/analysis.c',
 'deps/vorbis/lib/barkmel.c',
 'deps/vorbis/lib/bitrate.c',
 'deps/vorbis/lib/block.c',
 'deps/vorbis/lib/codebook.c',
 'deps/vorbis/lib/envelope.c',
 'deps/vorbis/lib/floor0.c',
 'deps/vorbis/lib/floor1.c',
 'deps/vorbis/lib/info.c',
 'deps/vorbis/lib/lookup.c',
 'deps/vorbis/lib/lpc.c',
 'deps/vorbis/lib/lsp.c',
 'deps/vorbis/lib/mapping0.c',
 'deps/vorbis/lib/mdct.c',
 'deps/vorbis/lib/psy.c',
 'deps/vorbis/lib/registry.c',
 'deps/vorbis/lib/res0.c',
 'deps/vorbis/lib/sharedbook.c',
 'deps/vorbis/lib/smallft.c',
 'deps/vorbis/lib/synthesis.c',
 'deps/vorbis/lib/vorbisfile.c',
 'deps/vorbis/lib/window.c']


includes    = ['deps/SDL/symbian', 'deps/vorbis/include', 'deps/vorbis/include/vorbis']
sysincludes = [EPOC32_INCLUDE, EPOC32_INCLUDE + "/libc", 'deps/ogg/include', 'deps/ogg/symbian']

defines     = []
if COMPILER == COMPILER_GCCE: 
    defines     = ['alloca=__builtin_alloca']

SymbianProgram( target, targettype,
    sources = sources,
    includes    = includes,
    sysincludes = sysincludes,
    libraries   = libraries,
    defines     = defines,
    epocstacksize = 8192,
    epocheapsize  = (0x400,0x100000),
    uid3 = uid3,
)

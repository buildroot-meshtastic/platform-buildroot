# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    Builder for buildroot platform
"""

from SCons.Script import COMMAND_LINE_TARGETS, AlwaysBuild, Default, DefaultEnvironment
import os

env = DefaultEnvironment()

env.Replace(
    AR=os.getenv("TARGET_AR"),
    AS=os.getenv("TARGET_AS"),
    CC=os.getenv("TARGET_CC"),
    CXX=os.getenv("TARGET_CXX"),
    LD=os.getenv("TARGET_LD"),
    OBJCOPY=os.getenv("TARGET_OBJCOPY"),
    RANLIB=os.getenv("TARGET_RANLIB")
)

env.Append(
    CFLAGS=os.getenv("TARGET_CFLAGS"),
    LDFLAGS=os.getenv("TARGET_LDFLAGS"),
    CXXFLAGS=os.getenv("TARGET_CXXFLAGS"),
)

print(env.Dump())

#
# Target: Build executable program
#

target_bin = env.BuildProgram()

#
# Target: Execute binary
#

exec_action = env.VerboseAction(
    "$SOURCE $PROGRAM_ARGS", "Executing $SOURCE")

AlwaysBuild(env.Alias("exec", target_bin, exec_action))
AlwaysBuild(env.Alias("upload", target_bin, exec_action))

#
# Target: Print binary size
#

# target_size = env.Alias("size", target_bin, env.VerboseAction(
#     "$SIZEPRINTCMD", "Calculating size $SOURCE"))
# AlwaysBuild(target_size)

#
# Default targets
#

Default([target_bin])

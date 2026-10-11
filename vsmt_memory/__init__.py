"""Rb-ERI entity memory as a plug-in for an RGB-D stream (guide: docs/PLUGIN.md).

Per frame the memory takes RGB, metric depth, intrinsics, a camera pose and instance masks, and returns the committed
frame program (NOOP / BIND / BIRTH / RETRACT / REACTIVATE) and the entity table (identity, state, version).  The
memory, recall, joint assignment, existence decisions and executor are the frozen functions of ``src/vsmt/lean_*.py``;
the default weights are the released ones (Hugging Face ``Embodied-SI/Rb-ERI``).  They were trained and evaluated on
ProcTHOR houses only; transfer to other scenes or sensors has not been tested.  ``RbERIMemory`` and ``VSMTMemory`` are
the same class (the latter is the name before decision D-224-NAME).

    from vsmt_memory import RbERIMemory, CameraIntrinsics, CameraPose

    memory = RbERIMemory.from_pretrained()                # SAM 2.1 front-end weights, seed 7
    result = memory.step(rgb, depth_m, intrinsics, pose, masks)
    for op in result.program: ...
    for entity in result.entities: ...
"""

from . import _repo  # noqa: F401  (puts the repository's src/ on sys.path)
from .conventions import CameraIntrinsics, CameraPose, to_user_world
from .memory import EntityRecord, FrameResult, Operation, RbERIMemory, VSMTMemory
from .weights import PretrainedWeights, load_pretrained

__all__ = ["CameraIntrinsics", "CameraPose", "EntityRecord", "FrameResult", "Operation", "PretrainedWeights",
           "RbERIMemory", "VSMTMemory", "load_pretrained", "to_user_world"]

from typing import Callable, NamedTuple, Optional

from dataclasses import dataclass, field, replace

@dataclass(frozen=True, slots=True)
class SetupFeatures:
    update_funcs:  bool = False
    external_func: bool = False
    fixed_1d_end: bool = False

@dataclass(frozen=True, slots=True)
class PerfFeatures:
    vec_spring_forces: bool = False
    vec_nib_forces:    bool = False
    vec_target_forces: bool = False
    check_corr_spring: bool = False
    check_corr_nib:    bool = False
    check_corr_target: bool = False

@dataclass(frozen=True, slots=True)
class LegacyFeatures:
    setup: SetupFeatures = field(default_factory=SetupFeatures)
    perf:  PerfFeatures  = field(default_factory=PerfFeatures)

_legacy_path = LegacyFeatures()

_updated_path = LegacyFeatures(
    setup=SetupFeatures(update_funcs=True, external_func=True),
    perf=PerfFeatures(
        vec_spring_forces=True,
        vec_nib_forces=True,
        vec_target_forces=True,
    ),
)

_debug_path = replace(
    _updated_path,
    perf=replace(
        _updated_path.perf,
        check_corr_spring=True,
        check_corr_nib=True,
        check_corr_target=True,
    ),
)

feature_selection = _debug_path

class ExtraParams(NamedTuple):
    class UpdateFuncs(NamedTuple):
        update_springs_func:                Optional[Callable] = None
        update_target_point_positions_func: Optional[Callable] = None
        update_beams_func:                  Optional[Callable] = None
        update_noninv_beams_func:           Optional[Callable] = None
        update_damped_springs_func:         Optional[Callable] = None

    update_funcs: UpdateFuncs
    external_force_func: Optional[Callable] = None

class NotBackCompat(Exception):
    pass
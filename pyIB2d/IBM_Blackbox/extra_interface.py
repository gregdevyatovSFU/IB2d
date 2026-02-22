from typing import Callable, NamedTuple, Optional


class _LegacyFeatures(NamedTuple):
    class SetupFeatures(NamedTuple):
        update_funcs: bool
        external_func: bool
        fix_beam_end: bool

    setup: SetupFeatures

legacy_path = _LegacyFeatures(
    setup=_LegacyFeatures.SetupFeatures(
        update_funcs=False,
        external_func=False,
        fix_beam_end=False
    )
)

updated_path = _LegacyFeatures(
    setup=_LegacyFeatures.SetupFeatures(
        update_funcs=True,
        external_func=True,
        fix_beam_end=True
    )
)


class ExtraParams(NamedTuple):
    class UpdateFuncs(NamedTuple):
        update_springs_func                : Optional[Callable] = None
        update_target_point_positions_func : Optional[Callable] = None
        update_beams_func                  : Optional[Callable] = None
        update_noninv_beams_func           : Optional[Callable] = None
        update_damped_springs_func         : Optional[Callable] = None

    update_funcs: UpdateFuncs
    external_force_func: Optional[Callable] = None

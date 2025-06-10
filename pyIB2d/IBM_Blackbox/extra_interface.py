from typing import NamedTuple


class _LegacyFeatures(NamedTuple):
    class SetupFeatures(NamedTuple):
        update_funcs: bool

    setup: SetupFeatures

legacy_path = _LegacyFeatures(
    setup=_LegacyFeatures.SetupFeatures(
        update_funcs=False
    )
)

updated_path = _LegacyFeatures(
    setup=_LegacyFeatures.SetupFeatures(
        update_funcs=True
    )
)


class ExtraParams(NamedTuple):
    class UpdateFuncs(NamedTuple):
        update_springs_func                : callable = None
        update_target_point_positions_func : callable = None
        update_beams_func                  : callable = None
        update_noninv_beams_func           : callable = None
        update_damped_springs_func         : callable = None

    update_funcs: UpdateFuncs

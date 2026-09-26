"""Blocking semantic asset check for Dagster materializations."""
from jev_common import JevClient

def semantic_asset_check(asset, *, question, text_metadata_key='content', threshold=0.8, client=None):
    import dagster as dg
    judge = client or JevClient(question, threshold=threshold)

    @dg.asset_check(asset=asset, blocking=True, name='jev_semantic_check')
    def check(context):
        event = context.get_latest_materialization_event()
        if event is None:
            return dg.AssetCheckResult(passed=False, metadata={'jev_route': 'failure'})
        value = event.dagster_event.event_specific_data.materialization.metadata.get(text_metadata_key)
        text = getattr(value, 'value', None)
        result = judge.decide(text)
        return dg.AssetCheckResult(passed=result['route'] == 'yes',
                                   metadata={'jev_route': result['route'],
                                             'jev_probability': result['probability'] or 0.0})
    return check

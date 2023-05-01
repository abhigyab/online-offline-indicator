from storage.key_vault_config import get_secret_value

cosmos_db_params = {
    'account_name': 'innercircledb',
    'account_key': get_secret_value('InnerCircleRecommendDbSecret'),
    'endpoint': 'https://innercircledb.documents.azure.com:443/',
    'db_name': 'InnerCircleRecommendDB',
    'events_table': 'events',
    'features_table': 'features',
    'weights_table': 'weights',
    'feedback_table': 'feedback',
    'tokens_table': 'tokens',
    'feature_users_table': 'feature_users',
    'partition_key': 'id',
}
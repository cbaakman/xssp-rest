from kombu import Exchange, Queue

# Celery
CELERY_BROKER_URL = 'amqp://guest@localhost'
CELERY_DEFAULT_QUEUE = 'xssp'
CELERY_QUEUES = (
    Queue('xssp', Exchange('xssp'), routing_key='xssp'),
)
CELERY_RESULT_BACKEND = 'redis://localhost/0'
CELERY_TRACK_STARTED = True

# xssp
XSSP_DATABANKS = ['/data/fasta/sprot.fasta', '/data/fasta/trembl.fasta']

# uploads
UPLOAD_FOLDER = '/tmp/xssp-rest/uploads'
ALLOWED_EXTENSIONS = ['bdb', 'bz2', 'cif', 'ent', 'gz', 'mcif', 'pdb']

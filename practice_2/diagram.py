from diagrams import Diagram
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.storage import PV, PVC, StorageClass

with Diagram("diagram", show=False):
    static = Ingress("domain.com/static") >> Service("svc") >> Pod("static")
    app = Ingress("domain.com") >> Service("svc")
    dbPod = Service("mariadb-svc")
    dbPod >> Pod("mariadb") >> PVC("pvc") << PV("pv") << StorageClass("sc")
    app >> Pod("app") >> dbPod

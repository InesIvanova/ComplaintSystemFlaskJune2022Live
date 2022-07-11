from resources.auth import RegisterResource, LoginResource
from resources.complaint import ComplaintsResource, ApproveComplaintResource, RejectComplaintResource

routes = (
    (RegisterResource, "/register/"),
    (LoginResource, "/login/"),
    (ComplaintsResource, "/complaint/"),
    (ApproveComplaintResource, "/complaint/<int:id>/approve/"),
    (RejectComplaintResource, "/complaint/<int:id>/reject/"),
)

# coding=utf-8
import logging
from .api_client import ScalrRestAPI

log = logging.getLogger(__name__)


class ScalrUserAPI(ScalrRestAPI):
    def role_create(self, role):
        """
        Create a new Role in the Environment.
        :param role: https://api-explorer.scalr.com/definitions/R/Role.html
        :return:
        """
        log.info(f"Creating role {role['name']}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/"
        return self.create(url, json=role)

    def role_delete(self, role_id):
        """
        Delete a Role from the Environment.
        :param role_id: int
        :return:
        """
        log.info(f"Deleting role {role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/"
        return self.delete(url)

    def role_edit(self, role_id, role):
        """
        Modify the attributes of a given Role.
        :param role_id: int
        :param role: https://api-explorer.scalr.com/definitions/R/Role.html
        :return:
        """
        log.info(f"Editing role {role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/"
        return self.patch(url, json=role)

    def role_get(self, role_id):
        """
        Retrieve detailed information about a given Role.
        :param role_id: int
        :return:
        """
        log.info(f"Fetching role {role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/"
        return self.fetch(url)

    def role_list(self, **params):
        """
        List all the Roles available in the Environment.
        :param builtinAutomation: list
        :param category: int
        :param id: int
        :param name: str
        :param os: str
        :param quickStart: bool
        :param quickStartGroup: str
        :param scope: str
        :param useScalrAgent: bool
        :return:
        """
        log.info(f"Listing roles")
        url = f"/api/v1beta0/user/{self.env_id}/roles/"
        return self.list(url, params=params)

    def role_clone(self, role_id, name):
        """
        Make a copy of an existing Role by cloning it.
        :param role_id: int
        :param name: str
        :return:
        """
        log.info(f"Cloning role {role_id} as {name}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/actions/clone/"
        return self.post(url, json={"name": name})

    def role_image_create(self, role_id, role_image):
        """
        Associates a new Image with a given Role. This will fail if an Image associated to the Role is in the same
        location than the Image you are trying to add.
        :param role_id: int
        :param role_image: https://api-explorer.scalr.com/definitions/R/RoleImage.html
        :return:
        """
        log.info(f"Associating image {role_image['image']['id']} to {role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/images/"
        return self.create(url, json=role_image)

    def role_image_delete(self, role_id, image_id):
        """
        Dis-associates an Image from a given Role.
        :param role_id: int
        :param image_id: str
        :return:
        """
        log.info(f"Dis-associating image {image_id} from role {role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/images/{image_id}/"
        return self.delete(url)

    def role_image_get(self, role_id, image_id):
        """
        Retrieve detailed information about an Image.
        :param role_id: int
        :param image_id: str
        :return:
        """
        log.info(f"Fetching image {image_id}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/images/{image_id}/"
        return self.fetch(url)

    def role_image_list(self, role_id, **params):
        """
        List all Images associated with a given Role.
        :param role_id: int
        :param image: str
        :param role: int
        :return:
        """
        log.info(f"Listing role images")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/images/"
        return self.list(url, params=params)

    def role_image_replace(self, role_id, image_id, role_image):
        """
        Replace an Image in-place in a given Role.
        :param role_id: int
        :param image_id: str
        :param role_image: https://api-explorer.scalr.com/definitions/R/RoleImage.html
        :return:
        """
        log.info(f"Replacing image {image_id} with {role_image['image']['id']} for role {role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/roles/{role_id}/images/{image_id}/actions/replace/"
        return self.post(url, json=role_image)

    def farm_role_create(self, farm_id, farm_role):
        """
        Create a new Farm Role in a Farm.
        :param farm_id: int
        :param farm_role: https://api-explorer.scalr.com/definitions/F/FarmRole.html
        :return:
        """
        log.info(f"Creating farm role {farm_role['alias']} for farm {farm_id}")
        url = f"/api/v1beta0/user/{self.env_id}/farms/{farm_id}/farm-roles/"
        return self.create(url, json=farm_role)

    def farm_role_delete(self, farm_role_id):
        """
        Remove a given Farm Role from its Farm.
        :param farm_role_id: int
        :return:
        """
        log.info(f"Deleting farm role {farm_role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/farm-roles/{farm_role_id}/"
        return self.delete(url)

    def farm_role_edit(self, farm_role_id, farm_role):
        """
        Modify the attributes of a Farm Role.
        :param farm_role_id: int
        :param farm_role: https://api-explorer.scalr.com/definitions/F/FarmRole.html
        :return:
        """
        log.info(f"Editing farm role {farm_role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/farm-roles/{farm_role_id}/"
        return self.patch(url, json=farm_role)

    def farm_role_get(self, farm_role_id):
        """
        Retrieve detailed information about a given Farm Role.
        :param farm_role_id: int
        :return:
        """
        log.info(f"Fetching farm role {farm_role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/farm-roles/{farm_role_id}/"
        return self.fetch(url)

    def farm_role_list(self, farm_id, **params):
        """
        List all the Farm Roles in a Farm.
        :param farm_id: int
        :param alias: str
        :param cloudLocation: int
        :param cloudPlatform: str
        :param farm: int
        :param id: int
        :param role: int
        :return:
        """
        log.info(f"Listing farm roles")
        url = f"/api/v1beta0/user/{self.env_id}/farms/{farm_id}/farm-roles/"
        return self.list(url, params=params)

    def farm_role_clone(self, farm_role_id, name, another_farm_role_id=None):
        """
        Clone a given FarmRole within current Farm or to another Farm.
        :param farm_role_id: int
        :param name: str
        :param another_farm_role_id: int (Optional)
        :return:
        """
        log.info(f"Cloning farm role {farm_role_id} as {name}")
        params = {"name": name}
        if another_farm_role_id:
            params["farm"] = {"id": another_farm_role_id}
        url = f"/api/v1beta0/user/{self.env_id}/farm-roles/{farm_role_id}/actions/clone/"
        return self.post(url, json=params)

    def farm_create(self, farm):
        """
        Create a new Farm in the Environment.
        :param farm: https://api-explorer.scalr.com/definitions/F/Farm.html
        :return:
        """
        log.info(f"Creating farm {farm['name']}")
        url = f"/api/v1beta0/user/{self.env_id}/farms/"
        return self.create(url, json=farm)

    def farm_delete(self, farm_id):
        """
        Delete a Farm from the Environment.
        :param farm_id: int
        :return:
        """
        log.info(f"Deleting farm {farm_id}")
        url = f"/api/v1beta0/user/{self.env_id}/farms/{farm_id}/"
        return self.delete(url)

    def farm_edit(self, farm_id, farm):
        """
        Modify the attributes of a Farm.
        :param farm_id: int
        :param farm: https://api-explorer.scalr.com/definitions/F/Farm.html
        :return:
        """
        log.info(f"Editing farm {farm_id}")
        url = f"/api/v1beta0/user/{self.env_id}/farms/{farm_id}/"
        return self.patch(url, json=farm)

    def farm_get(self, farm_id):
        """
        Retrieve detailed information about a given Farm.
        :param farm_id: int
        :return:
        """
        log.info(f"Fetching farm {farm_id}")
        url = f"/api/v1beta0/user/{self.env_id}/farms/{farm_id}/"
        return self.fetch(url)

    def farm_list(self, **params):
        """
        List all the Farms available in the Environment.
        :param id: int
        :param launchOrder: str
        :param name: str
        :param owner: int
        :param project: str
        :param status: str
        :param teams: list
        :param timezone: str
        :return:
        """
        log.info(f"Listing farms")
        url = f"/api/v1beta0/user/{self.env_id}/farms/"
        return self.list(url, params=params)

    def server_create(self, farm_role_id):
        """
        Launch a new Server for the specified Farm Role.
        :param farm_role_id: int
        :return:
        """
        log.info(f"Launching server for farm role {farm_role_id}")
        url = f"/api/v1beta0/user/{self.env_id}/servers/"
        return self.create(url, json={"farmRole": {"id": farm_role_id}})

    def server_get(self, server_id):
        """
        Retrieve detailed information about a Server.
        :param server_id: str
        :return:
        """
        log.info(f"Fetching server {server_id}")
        url = f"/api/v1beta0/user/{self.env_id}/servers/{server_id}/"
        return self.fetch(url)

    def server_list(self, **params):
        """
        List all the Servers that exist in the Environment.
        :param cloudLocation: str
        :param cloudPlatform: str
        :param cloudServerId: str
        :param farm: int
        :param farmRole: int
        :param hostname: str
        :param id: str
        :param index: int
        :param instanceType: str
        :param launchedBy: int
        :param launchReason: str
        :param privateIp: list
        :param publicIp: list
        :param status: str
        :return:
        """
        log.info(f"Listing servers")
        url = f"/api/v1beta0/user/{self.env_id}/servers/"
        return self.list(url, params=params)

    def server_reboot(self, server_id, hard_reboot=False):
        """
        Reboot a Server.
        :param server_id: str
        :param hard_reboot: bool
        :return:
        """
        log.info(f"Rebooting server {server_id}")
        url = f"/api/v1beta0/user/{self.env_id}/servers/{server_id}/actions/reboot/"
        return self.post(url, json={"hard": hard_reboot})

    def server_resume(self, server_id):
        """
        Resume a suspended Server.
        :param server_id: str
        :return:
        """
        log.info(f"Resuming suspended server {server_id}")
        url = f"/api/v1beta0/user/{self.env_id}/servers/{server_id}/actions/resume/"
        return self.post(url)

    def server_suspend(self, server_id):
        """
        Suspend a Server.
        :param server_id: str
        :return:
        """
        log.info(f"Suspending server {server_id}")
        url = f"/api/v1beta0/user/{self.env_id}/servers/{server_id}/actions/suspend/"
        return self.post(url)

    def server_sync(self, server_id):
        """
        Sync the Ansible Tower Configuration on the Server.
        :param server_id: str
        :return:
        """
        log.info(f"Syncing server {server_id}")
        url = f"/api/v1beta0/user/{self.env_id}/servers/{server_id}/actions/sync/"
        return self.post(url)

    def server_terminate(self, server_id, force_terminate=False):
        """
        Terminate a Server.
        :param server_id: str
        :param force_terminate: bool
        :return:
        """
        log.info(f"Terminating server {server_id}")
        url = f"/api/v1beta0/user/{self.env_id}/servers/{server_id}/actions/terminate/"
        return self.post(url, json={"force": force_terminate})

    def image_create(self, image):
        """
        Register a new Image in this Environment.
        :param image: https://api-explorer.scalr.com/definitions/I/Image.html
        :return:
        """
        log.info(f"Creating image {image['name']}")
        url = f"/api/v1beta0/user/{self.env_id}/images/"
        return self.create(url, json=image)

    def image_delete(self, image_id, **params):
        """
        Remove an Image from the Environment. By default this does not delete the underlying machine image from the
        Cloud it resides in.
        :param image_id: str
        :param deleteFromCloud: bool
        :return:
        """
        log.info(f"Deleting image {image_id}")
        url = f"/api/v1beta0/user/{self.env_id}/images/{image_id}/"
        return self.delete(url, params=params)

    def image_edit(self, image_id, image):
        """
        Modify the attributes of an Images. Currently only the name of the Image be can changed.
        :param image_id: str
        :param image: https://api-explorer.scalr.com/definitions/I/Image.html
        :return:
        """
        log.info(f"Editing image {image_id}")
        url = f"/api/v1beta0/user/{self.env_id}/images/{image_id}/"
        return self.patch(url, json=image)

    def image_get(self, image_id):
        """
        Retrieve detailed information about an Image.
        :param image_id: str
        :return:
        """
        log.info(f"Fetching image {image_id}")
        url = f"/api/v1beta0/user/{self.env_id}/images/{image_id}/"
        return self.fetch(url)

    def image_list(self, **params):
        """
        List all the Images available in the Environment.
        :param architecture: str
        :param cloudImageId: str
        :param cloudInitInstalled: bool
        :param cloudLocation: str
        :param cloudPlatform: str
        :param deprecated: bool
        :param id: str
        :param name: str
        :param os: str
        :param scalrAgentInstalled: bool
        :param scope: str
        :param source: str
        :param status: str
        :return:
        """
        log.info(f"Listing images")
        url = f"/api/v1beta0/user/{self.env_id}/images/"
        return self.list(url, params=params)

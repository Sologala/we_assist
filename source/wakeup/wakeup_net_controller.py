from controllers import base_controller
from modules.io_mod import net_protocol_component
from modules.io_mod import net_client_component

import wakeup_check_component
import wakeup_state_component

class wakeup_net_controller(base_controller.base_controller) :
    default_port = 23332
    def __init__(self):
        super().__init__()

    def initialize(self):
        super().initialize()

        protocol_component = net_protocol_component.net_protocol_component(self)
        self.components.append(protocol_component)
        self.components.append(net_client_component.net_client_component(self, '127.0.0.1', self.default_port, error_cb=self.on_error_cb, connected_cb=self.on_connected_cb))
        self.components.append(wakeup_check_component.wakeup_check_component(self, 5 * 60)) #5mins once
        self.components.append(wakeup_state_component.wakeup_state_component(self))
        for it in self.components :
            it.initialize()

    def destroy(self):
        super().destroy()
        for it in self.components:
            it.destroy()

    def on_error_cb(self, tpc_base, exception):
        print(' wakeup error: ', str(exception))
        check_component = self.get_component('wakeup_check_component')
        if check_component :
            check_component.is_client_good = False

    def on_connected_cb(self, tcp_base):
        print('wakeup : connected!')
        check_component = self.get_component('wakeup_check_component')
        if check_component:
            check_component.is_client_good = True


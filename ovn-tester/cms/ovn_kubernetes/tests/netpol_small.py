from cms.ovn_kubernetes.tests.netpol import NetPol


class NetpolSmall(NetPol):
    def __init__(self, config, cluster, global_cfg):
        super().__init__('netpol_small', config, cluster)

    def run(self, ovn, global_cfg):
        self.init(ovn, global_cfg)
        super().run(ovn, global_cfg, True)

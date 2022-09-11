import torch

from ptens_base import ptensor0 as _ptensor0


class ptensor0(torch.Tensor):

    @classmethod
    def zeros(self, _atoms, _nc):
        R=ptensor0(torch.zeros(_nc))
        R.atoms=_atoms
        return R
    
    @classmethod
    def randn(self, _atoms, _nc):
        R=ptensor0(torch.randn(_nc))
        R.atoms=_atoms
        return R


    # ---- Access --------------------------------------------------------------------------------------------


    def get_nc(self):
        return self.size(0)


    # ---- Operations ----------------------------------------------------------------------------------------

    
    def linmaps0(self):
        return Ptensor0_Linmaps0Fn.apply(self);

    def linmaps1(self):
        return Ptensor0_Linmaps1Fn.apply(self);

    def linmaps2(self):
        return Ptensor0_Linmaps2Fn.apply(self);


    # ---- I/O -----------------------------------------------------------------------------------------------


    def __str__(self):
        u=_ptensor0.view(self,self.atoms)
        return u.__str__()



# ------------------------------------------------------------------------------------------------------------


class Ptensor0_Linmaps0Fn(torch.autograd.Function):

    @staticmethod
    def forward(ctx,x):
        R=ptensor0.zeros(x.atoms,x.get_nc())
        u=_ptensor0.view(x,x.atoms)
        _ptensor0.view(R,R.atoms).add_linmaps(u)
        return R
        
    @staticmethod
    def backward(ctx,g):
        print("ddp")


class Ptensor0_Linmaps1Fn(torch.autograd.Function):

    @staticmethod
    def forward(ctx,x):
        R=ptensor1.zeros(x.atoms,x.get_nc())
        u=_ptensor0.view(x,x.atoms)
        _ptensor1.view(R,R.atoms).add_linmaps(u)
        return R
        
    @staticmethod
    def backward(ctx,g):
        print("ddp")


class Ptensor0_Linmaps2Fn(torch.autograd.Function):

    @staticmethod
    def forward(ctx,x):
        R=ptensor2.zeros(x.atoms,2*x.get_nc())
        u=_ptensor0.view(x,x.atoms)
        _ptensor2.view(R,R.atoms).add_linmaps(u)
        return R
        
    @staticmethod
    def backward(ctx,g):
        print("ddp")


# ------------------------------------------------------------------------------------------------------------


def linmaps0(x):
    return x.linmaps0()
    
def linmaps1(x):
    return x.linmaps1()
    
def linmaps2(x):
    return x.linmaps2()
    
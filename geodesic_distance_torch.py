import numpy as np
import torch
import matplotlib.pyplot as plt

def Get_Geodesic(source_data, target_data, dims=1000):
    source_data = torch.from_numpy(source_data)
    target_data = torch.from_numpy(target_data)
    u_s, s_s, v_s = torch.svd(source_data.t())
    u_t, s_t, v_t = torch.svd(target_data.t())

    pa = torch.mm(u_s.t(), u_t)

    p_s, cospa, p_t = torch.svd(pa)

    sinpa = torch.sqrt(1-torch.pow(cospa, 2))
    # rsd = torch.norm(sinpa, 1)# + 0.1 * torch.norm(torch.abs(p_s) - torch.abs(p_t), 2)
    sinpa = torch.where(torch.isnan(sinpa), torch.full_like(sinpa, 0), sinpa)
    rsd = torch.mean(torch.abs_(sinpa))
    return rsd, sinpa

if __name__ == '__main__':

    source_data = np.random.random(size=(4, 16))    ## source data, n x f, where n is the sample number, f is the dimension of the features, f should be larger than n
    target_data = np.random.random(size=(8, 16))     ## target data, m x f, where m is the sample number, f is the dimension of the features, f should be larger than f

    rsd, sinpa = Get_Geodesic(source_data, target_data)

    rsd = rsd.numpy()

    print("Geodesic distance from source to target:", rsd)

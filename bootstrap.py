import pandas as pd
import numpy as np
from scipy.stats import norm


def get_bootstrap(data_1, data_2, boot_subsamples=1000, statistic=np.mean, conf_level=0.95):
    """
    Params:
        data_1, data_2 - samples
        boot_subsamples - bootstrap subsamples quantity
        statistic - stat to use
        conf_level - confidence level (1 - alpha)
    
    Returns:
        dict with keys:
            "boot_data": stat diff for each subsample
            "quants": quants 
            "p_value": p_value                
    """
    
    
    # Forming a random sub samples with return, and appending passed 'statistic'
    data = []    
    for i in range(boot_subsamples): 
        samples_1 = data_1.sample(len(data_1), replace = True).values        
        samples_2 = data_2.sample(len(data_2), replace = True).values        
        data.append(statistic(samples_1) - statistic(samples_2))        
    
    # Converting to a DataFrame
    df = pd.DataFrame(data)
    
    # Defining a quantiles of distribution, based on passed 'conf_level'    
    left_quant  = (1 - conf_level) / 2
    right_quant = 1 - left_quant    
    quants      = df.quantile([left_quant, right_quant])
    
    # Calculating distribution of means
    p_1 = norm.cdf(x = 0, loc = np.mean(data), scale = np.std(data))
    p_2 = norm.cdf(x = 0, loc = -np.mean(data), scale = np.std(data))    
    
    # Calculating p-value
    p = min(p_1, p_2) * 2        
       
    return {"boot_data": data, 
            "quants": quants, 
            "p_value": p}


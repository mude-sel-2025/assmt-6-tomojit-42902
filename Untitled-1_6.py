    # ================================
# Task 3: Averaging effect (m>1)
# ================================
def task3_averaging(N=1000, m_list=[1, 2, 10, 100]):
    for name, dist in dists.items():

        fig, axes = plt.subplots(2, 2, figsize=(12,8))
        fig.suptitle(f"Averaging effect - {name}")
        
        for ax, m in zip(axes.flat, m_list):
            samples = np.mean(dist.rvs(size=(N,m)), axis=1)

            # WRITE_YOUR_CODE HERE TO FIND SIMULATED MEAN, VAR FROM SAMPLES
            # Simulated mean, var, and std of selected samples
            sim_mean = np.mean(samples)
            sim_var =  np.var(samples) 

            # WRITE_YOUR_CODE HERE TO FIND SIMULATED MEAN, VAR FROM DISTRIBUTION DEFINITIONS
            # Theoretical sample mean, var, and std
            theo_mu = dist.mean()    
            theo_var = dist.var()
            # this code block ends here

            ax.hist(samples, bins=20, density=True, alpha=0.7, color='orange')
            ax.set_title(f"m={m}")
            ax.grid(True)
            
            # WRITE_YOUR_CODE HERE TO ADD TITLE WITH THEORETICAL AND SIMULATED VALUES. WHAT WILL GO IN BRACES {}?
            ax.set_title(f"For m={m}, theoretical mean (CLT) ~ N({m:.3f}, {m:.3f}/{m} = {m:.3f})\n"
            f"simulated: for {N} {name} samples. avg={N:.3f}, Var={N:.3f}")
            # this code block ends here

            # WRITE_YOUR_CODE HERE TO OVERLAY THEORETICAL CLT RESULT ON EACH HISTOGRAM
            x = np.linspace(dist.ppf(0.001), dist.ppf(0.999), N)
            clt_dist = norm(loc=theo_mu, scale= np.sqrt(theo_var)/np.sqrt((m)))
            y = clt_dist.pdf(x)
            ax.plot(x, y, 'r-', lw=2)
            # this code block ends here

        plt.tight_layout(rect=[0,0,1,0.95])
    
    
    
    # ================================
# Run main if this script is executed
# ================================
if __name__ == "__main__":
    #print("Task 1: Plot PDFs")
    #task1_plot_pdfs()
    
    # # print("Task 2: Raw Sampling Histograms")
     #task2_histograms()
    
    # # print("Task 3: Averaging Effect")
    task3_averaging()
    
    # print("Task 4: Variance Scaling")
    # task4_variance_scaling()
    
    # print("Task 5: Mean vs Standard Deviation")
    # task5_mean_std()

plt.show() # do not comment this out
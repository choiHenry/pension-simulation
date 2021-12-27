from simulation import simulate

if __name__ == "__main__":
    simulate("resultsNoSubsidy", rp_subsidy=False)
    simulate("resultsNoSubsidy", rp_subsidy=True)
    simulate("resultsSubsidyCap", rp_subsidy=True, subsidy_cap=329)

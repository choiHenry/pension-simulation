import pandas as pd
from pension import Pension

def simulate(outFileName, rp_subsidy=True, subsidy_cap=None):
    df_1970 = pd.read_csv('../data/new/wage_history_1970.csv')
    df_1980 = pd.read_csv('../data/new/wage_history_1980.csv')
    df_1990 = pd.read_csv('../data/new/wage_history_1990.csv')
    df_2000 = pd.read_csv('../data/new/wage_history_2000.csv')

    df_1970_group_1 = df_1970[['year', 'group_1']]
    df_1970_group_1.columns = ['year', 'wage']
    df_1970_group_2 = df_1970[['year', 'group_2']]
    df_1970_group_2.columns = ['year', 'wage']
    df_1970_group_3 = df_1970[['year', 'group_3']]
    df_1970_group_3.columns = ['year', 'wage']
    df_1970_group_4 = df_1970[['year', 'group_4']]
    df_1970_group_4.columns = ['year', 'wage']
    df_1970_group_5 = df_1970[['year', 'group_5']]
    df_1970_group_5.columns = ['year', 'wage']
    df_1970_group_6 = df_1970[['year', 'group_6']]
    df_1970_group_6.columns = ['year', 'wage']

    pension_1970_group_1 = Pension(df_1970_group_1, rp_entitlement_year=2025, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1970_group_2 = Pension(df_1970_group_2, military_year=1991, rp_entitlement_year=2026, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1970_group_3 = Pension(df_1970_group_3, rp_entitlement_year=2025, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1970_group_4 = Pension(df_1970_group_4, delivery_year=1999, rp_entitlement_year=2035, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1970_group_5 = Pension(df_1970_group_5, military_year=1990, rp_entitlement_year=2031, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1970_group_6 = Pension(df_1970_group_6, delivery_year=1999, rp_entitlement_year=2031, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    
    results_1970 = pd.concat([pension_1970_group_1.dc(), pension_1970_group_2.dc(), pension_1970_group_3.dc(),
                          pension_1970_group_4.dc(), pension_1970_group_5.dc(), pension_1970_group_6.dc()])
    results_1970.index = [1, 2, 3, 4, 5, 6]
    results_1970.index.name = '집단'
    results_1970.to_csv(f'../data/new/{outFileName}_1970.csv')
    
    df_1980_group_1 = df_1980[['year', 'group_1']]
    df_1980_group_1.columns = ['year', 'wage']
    df_1980_group_2 = df_1980[['year', 'group_2']]
    df_1980_group_2.columns = ['year', 'wage']
    df_1980_group_3 = df_1980[['year', 'group_3']]
    df_1980_group_3.columns = ['year', 'wage']
    df_1980_group_4 = df_1980[['year', 'group_4']]
    df_1980_group_4.columns = ['year', 'wage']
    df_1980_group_5 = df_1980[['year', 'group_5']]
    df_1980_group_5.columns = ['year', 'wage']
    df_1980_group_6 = df_1980[['year', 'group_6']]
    df_1980_group_6.columns = ['year', 'wage']

    pension_1980_group_1 = Pension(df_1980_group_1, rp_entitlement_year=2035, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1980_group_2 = Pension(df_1980_group_2, military_year=2001, rp_entitlement_year=2036, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1980_group_3 = Pension(df_1980_group_3, rp_entitlement_year=2035, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1980_group_4 = Pension(df_1980_group_4, delivery_year=2009, rp_entitlement_year=2045, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1980_group_5 = Pension(df_1980_group_5, military_year=2000, rp_entitlement_year=2041, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1980_group_6 = Pension(df_1980_group_6, delivery_year=2009, rp_entitlement_year=2041, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)

    results_1980 = pd.concat([pension_1980_group_1.dc(), pension_1980_group_2.dc(), pension_1980_group_3.dc(),
                            pension_1980_group_4.dc(), pension_1980_group_5.dc(), pension_1980_group_6.dc()])
    results_1980.index = [1, 2, 3, 4, 5, 6]
    results_1980.index.name = '집단'
    results_1980.to_csv(f'../data/new/{outFileName}_1980.csv')

    df_1990_group_1 = df_1990[['year', 'group_1']]
    df_1990_group_1.columns = ['year', 'wage']
    df_1990_group_2 = df_1990[['year', 'group_2']]
    df_1990_group_2.columns = ['year', 'wage']
    df_1990_group_3 = df_1990[['year', 'group_3']]
    df_1990_group_3.columns = ['year', 'wage']
    df_1990_group_4 = df_1990[['year', 'group_4']]
    df_1990_group_4.columns = ['year', 'wage']
    df_1990_group_5 = df_1990[['year', 'group_5']]
    df_1990_group_5.columns = ['year', 'wage']
    df_1990_group_6 = df_1990[['year', 'group_6']]
    df_1990_group_6.columns = ['year', 'wage']

    pension_1990_group_1 = Pension(df_1990_group_1, rp_entitlement_year=2045, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1990_group_2 = Pension(df_1990_group_2, military_year=2011, rp_entitlement_year=2046, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1990_group_3 = Pension(df_1990_group_3, rp_entitlement_year=2045, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1990_group_4 = Pension(df_1990_group_4, delivery_year=2019, rp_entitlement_year=2055, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1990_group_5 = Pension(df_1990_group_5, military_year=2010, rp_entitlement_year=2051, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_1990_group_6 = Pension(df_1990_group_6, delivery_year=2019, rp_entitlement_year=2051, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)

    results_1990 = pd.concat([pension_1990_group_1.dc(), pension_1990_group_2.dc(), pension_1990_group_3.dc(),
                            pension_1990_group_4.dc(), pension_1990_group_5.dc(), pension_1990_group_6.dc()])
    results_1990.index = [1, 2, 3, 4, 5, 6]

    results_1990.index.name = '집단'
    results_1990.to_csv(f'../data/new/{outFileName}_1990.csv')

    df_2000_group_1 = df_2000[['year', 'group_1']]
    df_2000_group_1.columns = ['year', 'wage']
    df_2000_group_2 = df_2000[['year', 'group_2']]
    df_2000_group_2.columns = ['year', 'wage']
    df_2000_group_3 = df_2000[['year', 'group_3']]
    df_2000_group_3.columns = ['year', 'wage']
    df_2000_group_4 = df_2000[['year', 'group_4']]
    df_2000_group_4.columns = ['year', 'wage']
    df_2000_group_5 = df_2000[['year', 'group_5']]
    df_2000_group_5.columns = ['year', 'wage']
    df_2000_group_6 = df_2000[['year', 'group_6']]
    df_2000_group_6.columns = ['year', 'wage']

    pension_2000_group_1 = Pension(df_2000_group_1, rp_entitlement_year=2055, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_2000_group_2 = Pension(df_2000_group_2, military_year=2021, rp_entitlement_year=2056, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_2000_group_3 = Pension(df_2000_group_3, rp_entitlement_year=2055, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_2000_group_4 = Pension(df_2000_group_4, delivery_year=2029, rp_entitlement_year=2065, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_2000_group_5 = Pension(df_2000_group_5, military_year=2020, rp_entitlement_year=2061, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)
    pension_2000_group_6 = Pension(df_2000_group_6, delivery_year=2029, rp_entitlement_year=2061, rp_subsidy=rp_subsidy, subsidy_cap=subsidy_cap)

    results_2000 = pd.concat([pension_2000_group_1.dc(), pension_2000_group_2.dc(), pension_2000_group_3.dc(),
                            pension_2000_group_4.dc(), pension_2000_group_5.dc(), pension_2000_group_6.dc()])
    results_2000.index = [1, 2, 3, 4, 5, 6]
    results_2000.index.name = '집단'
    results_2000.to_csv(f'../data/new/{outFileName}_2000.csv')
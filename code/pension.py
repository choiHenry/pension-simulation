import numpy as np
import pandas as pd
import math

def annual_saving(row, rp_enforcement_year, subsidy_cap):
    if (row['year'] >= rp_enforcement_year) and (row['wage'] < subsidy_cap):
        return 12 * row['wage'] * 0.0417 * 3
    elif (row['year'] >= rp_enforcement_year):
        return 12 * row['wage'] * 0.0417 * 2
    else:
        return np.nan

class Pension:

    def __init__(self, wage_history=None, delivery_year=None, military_year=None, rp_entitlement_year=None, rp_subsidy=True, subsidy_cap=None):
        
        self.wage_history = wage_history
        self.delivery_year = delivery_year
        self.military_year = military_year
        self.p = {
            1988: 2.4, 1989: 2.4, 1990: 2.4, 1991: 2.4, 1992: 2.4, 1993: 2.4, 1994: 2.4, 1995: 2.4, 1996: 2.4, 1997: 2.4, 1998: 2.4,
            1999: 1.8, 2000: 1.8, 2001: 1.8, 2002: 1.8, 2003: 1.8, 2004: 1.8, 2005: 1.8, 2006: 1.8, 2007: 1.8,
            2008: 1.5, 2009: 1.485, 2010: 1.470, 2011: 1.455, 2012: 1.440, 2013: 1.425, 2014: 1.410, 2015: 1.395, 2016: 1.380, 2017: 1.365, 2018: 1.350, 2019: 1.335, 2020: 1.320,
            2021: 1.305, 2022: 1.290, 2023: 1.275, 2024: 1.260, 2025: 1.245, 2026: 1.230, 2027: 1.215, 2028: 1.2
        }
        
        # 2020 기준으로 A(실질임금 상승률을 반영한 2018-2020 평균 가입자평균소득월액) 계산
        self.A = sum([259.9734, 259.9734/1.021, 259.9734/1.021**2]) / 3 
        self.delivery_credit = 1
        self.military_credit = 0.5
        self.rp_enforcement_year = 2020
        self.rp_entitlement_year = rp_entitlement_year
        self.rp_subsidy = rp_subsidy
        self.subsidy_cap = subsidy_cap
    
    def national_pension(self):
        
        """
        물가상승률 2%
        실질임금상승률 2.1%
        실질금리 2%
        """
        
        # 수급시점 기준으로 연금액을 산정: 수급연령 65세
        entitlement_year = self.wage_history.iloc[-1, 0] + 1
        print(f"수급시점: {entitlement_year}")
        print(f"2020년 기준 A: {self.A}")
        
        # A: 연금수급 전 3년 평균소득월액의 평균액(실질임금상승률 2.1% 반영)

        A = self.A
        
        # 월소득 -> 기준소득월액
        self.wage_history['wage_with_upper_limit'] = self.wage_history['wage']\
                                                        .apply(lambda wage: min(wage, 504))
        
            
        # 2020년 기준으로 B 계산
        self.wage_history['standard_wage'] = self.wage_history['wage_with_upper_limit']\
                                                .apply(lambda wage: math.floor(wage * 10) / 10 if not pd.isna(wage) else wage)
        
        B = self.wage_history['standard_wage'].mean()

        print(f"2020년 기준 B: {B}")
        
        # C, Y 계산
        if self.delivery_year:
            if self.delivery_year > 2028:
                Y = 1.2
            else:
                Y = self.p[self.delivery_year]
            C = self.delivery_credit
        elif self.military_year:
            Y = self.p[self.military_year]
            C = self.military_credit
        else:
            Y = 0
            C = 0
        print(f"Y: {Y}")
        print(f"C: {C}")
        
        # X 계산
        X = 1.2
        print(f"X: {X}")
        
        # n 계산: 실업기간에는 국민연금 미가입 상태로 가정
        P = self.wage_history['standard_wage'].count()
        n = max(0, P - 20)
        print(f"P: {P}\nn: {n}")
        
        # P_n 계산
        self.wage_history['P_n'] = self.wage_history\
                                    .apply(lambda row: self.p[row['year']] if row['year'] <= 2028 else 1.2, axis=1)
        
        # A+B 계산
        self.wage_history['A+B'] = self.wage_history\
                                    .apply(lambda row: A+B if row['year'] >= 1999 else A+0.75*B, axis=1)
        
        # A+B x P_n
        self.wage_history['(A+B)*P_n'] = self.wage_history\
                                    .apply(lambda row: row['A+B'] * row['P_n'] if not pd.isna(row['standard_wage']) else np.nan, axis=1)
        
        intermediate_sum = self.wage_history['(A+B)*P_n'].sum()
        total = (intermediate_sum + (Y * (A + A) * C) + (X * (A + (1/2 * A))* 6)) * (1 + 0.05*n) / P
        print(f"2020년 기준 수급시점({entitlement_year})의 노령연금액: {total}")
        
        r = 1 + 0.02 / 12
        monthly = (1-r) / (1 - r**12) * total
        print(f"2020년 가치로 환산한 수급시점 {entitlement_year}의 노령연금 월지급액(annuity): {monthly}")
        
        return B, pd.DataFrame.from_dict({'국민연금 월지급액': [monthly], '생애평균소득': [B], '소득대체율': [monthly / B], '평균임금대비': [monthly / A]})
    
    def dc(self):
        """
        dc 방식
        적립률 8.3% + 정부 4.17% 보조
        연금비율 5%
        실질수익률 4%
        보험요율 8.3%
        실질금리 2%
        """
        if self.rp_subsidy:
            if self.subsidy_cap:
                self.wage_history['annual_saving'] = self.wage_history.apply(lambda row: annual_saving(row, self.rp_enforcement_year, self.subsidy_cap), axis=1)
            else:                        
                self.wage_history['annual_saving'] = self.wage_history\
                                                        .apply(lambda row: 12 * row['wage'] * 0.0417 * 3 if row['year'] >= self.rp_enforcement_year else np.nan, axis=1)
        else:
            self.wage_history['annual_saving'] = self.wage_history\
                                                    .apply(lambda row: 12 * row['wage'] * 0.0417 * 2 if row['year'] >= self.rp_enforcement_year else np.nan, axis=1)

        self.wage_history['annual_reserve'] = self.wage_history\
                                                .apply(lambda row: row['annual_saving'] * 1.04 ** (self.rp_entitlement_year - row['year']), axis=1)
        rp_fund = self.wage_history['annual_reserve'].sum()
        print(f"퇴직연금 적립액: {rp_fund}")
        
        rp_annuity = 0.05 * rp_fund
        r = 1 + 0.02 / 12
        rp_monthly = (1-r) / (1 - r**12) * rp_annuity
        print(f"퇴직연금 월지급액: {rp_monthly}")
        np_result = self.national_pension()
        A = self.A
        B = np_result[0]
        np_monthly = np_result[1].iloc[0, 0]
        
        return pd.concat([np_result[1], pd.DataFrame.from_dict({'퇴직연금 월지급액': [rp_monthly], '합산연금액': [rp_monthly + np_monthly], '합산소득대체율': [(rp_monthly+np_monthly) / B], '평균임금대비': [(rp_monthly+np_monthly) / A]})], axis=1)
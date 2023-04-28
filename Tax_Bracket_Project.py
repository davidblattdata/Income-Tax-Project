# -*- coding: utf-8 -*-

###Returns Federal and State of California tax for 2023 income

#Runs until input is x
while True:    
    amount = input('Income or (x)--exit: ')
    if amount == 'x':
        print('Program ending...')
        break
    amount = float(amount)

            
    #Federal tax brackets for single people (1st) and married (2nd)
    fed_brackets = {0: 0, 
                0.10: [10275, 20550], 0.12: [41775, 83550], 
                0.22: [89075, 178150], 0.24: [170050, 340100], 
                0.32: [215950, 431900], 0.35: [539900, 647850]}
    
    #California state brackets
    state_cali_brackets = {0: 0, 
                           0.01: [10099, 20198], 0.02: [23942, 47884], 
                           0.04: [37788, 75576], 0.06: [52455, 104910], 
                           0.08: [66295, 132590], 0.093: [338639, 677278], 
                           0.103: [406364, 812728], 0.113: [677275, 1354550]}
    
    #Variables for each Federal bracket
    s_bracket_10 = fed_brackets[0.10][0]
    s_bracket_12 = fed_brackets[0.12][0]
    s_bracket_22 = fed_brackets[0.22][0]
    s_bracket_24 = fed_brackets[0.24][0]
    s_bracket_32 = fed_brackets[0.32][0]
    s_bracket_35 = fed_brackets[0.35][0]
    
    m_bracket_10 = fed_brackets[0.10][1]
    m_bracket_12 = fed_brackets[0.12][1]
    m_bracket_22 = fed_brackets[0.22][1]
    m_bracket_24 = fed_brackets[0.24][1]
    m_bracket_32 = fed_brackets[0.32][1]
    m_bracket_35 = fed_brackets[0.35][1]
    
    #Variables for each California bracket.
    sc_bracket_01 = state_cali_brackets[0.01][0]
    sc_bracket_02 = state_cali_brackets[0.02][0]
    sc_bracket_04 = state_cali_brackets[0.04][0]
    sc_bracket_06 = state_cali_brackets[0.06][0]
    sc_bracket_08 = state_cali_brackets[0.08][0]
    sc_bracket_093 = state_cali_brackets[0.093][0]
    sc_bracket_103 = state_cali_brackets[0.103][0]
    sc_bracket_113 = state_cali_brackets[0.113][0]
    
    mc_bracket_01 = state_cali_brackets[0.01][1]
    mc_bracket_02 = state_cali_brackets[0.02][1]
    mc_bracket_04 = state_cali_brackets[0.04][1]
    mc_bracket_06 = state_cali_brackets[0.06][1]
    mc_bracket_08 = state_cali_brackets[0.08][1]
    mc_bracket_093 = state_cali_brackets[0.093][1]
    mc_bracket_103 = state_cali_brackets[0.103][1]
    mc_bracket_113 = state_cali_brackets[0.113][1]
    
    #Equations for set amounts (Federal)
    seq10 = 0.10 * s_bracket_10
    seq12 = 0.12 * (s_bracket_12 - s_bracket_10)
    seq22 = 0.22 * (s_bracket_22 - s_bracket_12)
    seq24 = 0.24 * (s_bracket_24 - s_bracket_22)
    seq32 = 0.32 * (s_bracket_32 - s_bracket_24)
    seq35 = 0.35 * (s_bracket_35 - s_bracket_32)
    
    meq10 = 0.10 * m_bracket_10
    meq12 = 0.12 * (m_bracket_12 - m_bracket_10)
    meq22 = 0.22 * (m_bracket_22 - m_bracket_12)
    meq24 = 0.24 * (m_bracket_24 - m_bracket_22)
    meq32 = 0.32 * (m_bracket_32 - m_bracket_24)
    meq35 = 0.35 * (m_bracket_35 - m_bracket_32)
    
    #Equations for set amounts (state -- cali)
    sceq01 = 0.01 * sc_bracket_01
    sceq02 = 0.02 * (sc_bracket_02 - sc_bracket_01)
    sceq04 = 0.04 * (sc_bracket_04 - sc_bracket_02)
    sceq06 = 0.06 * (sc_bracket_06 - sc_bracket_04)
    sceq08 = 0.08 * (sc_bracket_08 - sc_bracket_06)
    sceq093 = 0.093 * (sc_bracket_093 - sc_bracket_08)
    sceq103 = 0.103 * (sc_bracket_103 - sc_bracket_093)
    sceq113 = 0.113 * (sc_bracket_113 - sc_bracket_103)
    
    mceq01 = 0.01 * mc_bracket_01
    mceq02 = 0.02 * (mc_bracket_02 - mc_bracket_01)
    mceq04 = 0.04 * (mc_bracket_04 - mc_bracket_02)
    mceq06 = 0.06 * (mc_bracket_06 - mc_bracket_04)
    mceq08 = 0.08 * (mc_bracket_08 - mc_bracket_06)
    mceq093 = 0.093 * (mc_bracket_093 - mc_bracket_08)
    mceq103 = 0.103 * (mc_bracket_103 - mc_bracket_093)
    mceq113 = 0.113 * (mc_bracket_113 - mc_bracket_103)
    
    #Equations for specific amounts (Federal)
    
    aeq10 = 0.10 * amount
    
    aseq12 = 0.12 * (amount - s_bracket_10)
    aseq22 = 0.22 * (amount - s_bracket_12)
    aseq24 = 0.24 * (amount - s_bracket_22)
    aseq32 = 0.32 * (amount - s_bracket_24)
    aseq35 = 0.35 * (amount - s_bracket_32)
    aseq37 = 0.37 * (amount - s_bracket_35)
    
    ameq12 = 0.12 * (amount - m_bracket_10)
    ameq22 = 0.22 * (amount - m_bracket_12)
    ameq24 = 0.24 * (amount - m_bracket_22)
    ameq32 = 0.32 * (amount - m_bracket_24)
    ameq35 = 0.35 * (amount - m_bracket_32)
    ameq37 = 0.37 * (amount - m_bracket_35)
    
    #Equations for specific amounts (state -- cali)
    asceq01 = 0.01 * amount
    asceq02 = 0.02 * (amount - sc_bracket_01)
    asceq04 = 0.04 * (amount - sc_bracket_02)
    asceq06 = 0.06 * (amount - sc_bracket_04)
    asceq08 = 0.08 * (amount - sc_bracket_06)
    asceq093 = 0.093 * (amount - sc_bracket_08)
    asceq103 = 0.103 * (amount - sc_bracket_093)
    asceq113 = 0.113 * (amount - sc_bracket_103)
    asceq123 = 0.123 * (amount - sc_bracket_113)
    
    amceq01 = 0.01 * amount
    amceq02 = 0.02 * (amount - mc_bracket_01)
    amceq04 = 0.04 * (amount - mc_bracket_02)
    amceq06 = 0.06 * (amount - mc_bracket_04)
    amceq08 = 0.08 * (amount - mc_bracket_06)
    amceq093 = 0.093 * (amount - mc_bracket_08)
    amceq103 = 0.103 * (amount - mc_bracket_093)
    amceq113 = 0.113 * (amount - mc_bracket_103)
    amceq123 = 0.123 * (amount - mc_bracket_113)
    
    #Function that returns the amount that a single person is taxed
    def single_bracket_calc_fed(amount):
        if amount <= s_bracket_10:
            tax = aeq10
        elif amount <= s_bracket_12:
            tax = seq10 + aseq12
        elif amount <= s_bracket_22:
            tax = seq10 + seq12 + aseq22
        elif amount <= s_bracket_24:
            tax = seq10 + seq12 + seq22 + aseq24
        elif amount <= s_bracket_32:
            tax = seq10 + seq12 + seq22 + seq24 + aseq32
        elif amount <= s_bracket_35:
            tax = seq10 + seq12 + seq22 + seq24 + seq32 + aseq35
        else:
            tax = seq10 + seq12 + seq22 + seq24 + seq32 + seq35 + aseq37
        return tax
    
    #Function that returns the taxed amount of a married person
    def married_bracket_calc_fed(amount):
        if amount <= m_bracket_10:
            tax = aeq10
        elif amount <= m_bracket_12:
            tax = meq10 + ameq12
        elif amount <= m_bracket_22:
            tax = meq10 + meq12 + ameq22
        elif amount <= m_bracket_24:
            tax = meq10 + meq12 + meq22 + ameq24
        elif amount <= m_bracket_32:
            tax = meq10 + meq12 + meq22 + meq24 + ameq32
        elif amount <= m_bracket_35:
            tax = meq10 + meq12 + meq22 + meq24 + meq32 + ameq35
        else:
            tax = meq10 + meq12 + meq22 + meq24 + meq32 + meq35 + ameq37
        return tax
    
    #Function returns single state tax (cali)
    def single_bracket_calc_cali(amount):
        if amount < sc_bracket_01:
            tax = asceq01
        elif amount < sc_bracket_02:
            tax = sceq01 + asceq02
        elif amount < sc_bracket_04:
            tax = sceq01 + sceq02 + asceq04
        elif amount < sc_bracket_06:
            tax = sceq01 + sceq02 + sceq04 + asceq06
        elif amount < sc_bracket_08:
            tax = sceq01 + sceq02 + sceq04 + sceq06 + asceq08
        elif amount < sc_bracket_093:
            tax = sceq01 + sceq02 + sceq04 + sceq06 + sceq08 + asceq093
        elif amount < sc_bracket_103:
            tax = sceq01 + sceq02 + sceq04 + sceq06 + sceq08 + sceq093 + asceq103
        elif amount < sc_bracket_113:
            tax = sceq01 + sceq02 + sceq04 + sceq06 + sceq08 + sceq093 + sceq103
            + asceq113
        else:
            tax = sceq01 + sceq02 + sceq04 + sceq06 + sceq08 + sceq093 + sceq103 + sceq113 + asceq123
            
        return tax
    
    #Function returns married state tax (cali)
    def married_bracket_calc_cali(amount):
        if amount < mc_bracket_01:
            tax = amceq01
        elif amount < mc_bracket_02:
            tax = mceq01 + amceq02
        elif amount < mc_bracket_04:
            tax = mceq01 + mceq02 + amceq04
        elif amount < mc_bracket_06:
            tax = mceq01 + mceq02 + mceq04 + amceq06
        elif amount < mc_bracket_08:
            tax = mceq01 + mceq02 + mceq04 + mceq06 + amceq08
        elif amount < mc_bracket_093:
            tax = mceq01 + mceq02 + mceq04 + mceq06 + mceq08 + amceq093
        elif amount < mc_bracket_103:
            tax = mceq01 + mceq02 + mceq04 + mceq06 + mceq08 + mceq093 + amceq103
        elif amount < mc_bracket_113:
            tax = mceq01 + mceq02 + mceq04 + mceq06 + mceq08 + mceq093 + mceq103 + amceq113
        else:
            tax = mceq01 + mceq02 + mceq04 + mceq06 + mceq08 + mceq093 + mceq103 + mceq113 + amceq123
        return tax
    
    
    #Tax calculations to print
    single_tax_fed = single_bracket_calc_fed(amount) 
    single_tax_cali = single_bracket_calc_cali(amount)
    
    married_tax_fed = married_bracket_calc_fed(amount)
    married_tax_cali = married_bracket_calc_cali(amount)
    
    total_single_tax = single_tax_fed + single_tax_cali
    total_married_tax = married_tax_fed + married_tax_cali
    
    net_single = amount - total_single_tax
    net_married = amount - total_married_tax
    difference = net_married - net_single
    net_single_month = net_single / 12
    net_married_month = net_married / 12
    
    
    #Tax calculations formatted
    net_single_formatted = "{:,}".format(round(net_single))
    net_married_formatted = "{:,}".format(round(net_married))
    amount_formatted = "{:,}".format(round(amount))
    net_single_month_formatted = "{:,}".format(round(net_single_month))
    net_married_month_formatted = "{:,}".format(round(net_married_month))
    single_tax_fed_formatted = "{:,}".format(round(single_tax_fed))
    single_tax_cali_formatted = "{:,}".format(round(single_tax_cali))
    married_tax_fed_formatted = "{:,}".format(round(married_tax_fed))
    married_tax_cali_formatted = "{:,}".format(round(married_tax_cali))
    difference_formatted = "{:,}".format(round(difference))
    
    #Basic User Interface
    def user_interface():
        print("\nTax on $" + amount_formatted + ' if you are single: \n\tFederal Tax: $' + single_tax_fed_formatted + ' \n\tState -- Cali: $' + single_tax_cali_formatted)
        print('\tNet after tax: $' + net_single_formatted + ' \n\t or $' + net_single_month_formatted + ' per month' + '\n\n')
        print("Tax on $" + amount_formatted + ' if you are married: \n\tFederal Tax: $' 
              + married_tax_fed_formatted + ' \n\tState -- Cali: $' 
              + married_tax_cali_formatted)
        print('\tNet after tax: $' + net_married_formatted + ' \n\t or $' + net_married_month_formatted + ' per month')
        
        print("\nDifference of filing married verses single: $" + difference_formatted)
    
    #Continues until you exit the program
    while True:
    
        #Function for advanced features
        def advanced_features():
            children = input('How many children do you have: ')
            children = int(children)
            return children
            
        #User Interface Results
        selection = input('(s)--standard, (a)--advanced, or (x)--exit: ')
        if selection.lower() == 'x':
            break
        elif selection.lower() == 'a':
            children = advanced_features()
            
            amount_children = 2000 * children
            single_net_child_ded = net_single + amount_children
            married_net_child_ded = net_married + amount_children
            
            amount_children_formatted = "{:,}".format(round(amount_children))
            married_net_child_ded_formatted = "{:,}".format(round(married_net_child_ded))
            
            user_interface()
            
            print('\nOther deductions: ')
            print('\tChildren deductions: $' + str(amount_children))
            print('\n\tAdjusted net income (married): $' + str(married_net_child_ded_formatted))
        else: 
            user_interface()


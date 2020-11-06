
import sympy as sp
sp.init_printing()
income, a, leisure_hours, non_working_income, work_hours_contract, work_hours_available, wage_hourly_contract = sp.symbols('income, a, leisure_hours,                                                                                   non_working_income, work_hours_contract, work_hours_available, wage_hourly_contract')

leisure_hours = work_hours_available - work_hours_contract

working_utility = sp.log(income) + (a * leisure_hours)

idleness_utility = (non_working_income, work_hours_available)

working_contract = wage_hourly_contract * (work_hours_contract - leisure_hours) + non_working_income - income



# voluntary exchange condition
VE = working_utility - idleness_utility >= 0

if VE == True:
    print('It is preferable to have a job. This is a participation condition and it says  that  the  worker  chooses  working  rather  than  being  idle.  And  this  happens  under voluntary exchange even though the worker is not determining the optimal number of hours in order to maximize utility. In fact the number of hours that maximize utility could be lower than those established in the contract, but it is a regular  condition  imposed  for  contracts  as  is  the  case  in  Principal-Agent relationships.')
else:
    print('Having a job isn\'t worth it.')
    
# gaming condition 
    
available_tickets = iN

ticket_cost = ib

lottery_revenue = available_tickets * ticket_cost    

expected_monetary_prize = ( (available_tickets-1)*ticket_cost*(1/available_tickets) ) – ( ticket_cost * (available_tickets-(1/available_tickets)) )

expected_utility_to_win =   (1/available_tickets)* U(M+ ticket_cost(available_tickets-1), work_hours_available) + (available_tickets-(1/available_tickets) ) * U(wage_hourly_contract * work_hours_contract + non_working_income-ticket_cost, leisure_hours)

utility_of_not_buying_the_ticket = U(wage_hourly_contract * work_hours_contract + non_working_income, leisure_hours)
GC = expected_utility_to_win - utility_of_not_buying_the_ticket >= 0.    
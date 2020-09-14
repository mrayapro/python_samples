##def stack_ops(my_action,my_tenancy,my_stack):
##  if my_action=='stop':
##''' Mani Commented this region to exclude GG from QM
##    #GG
##    print("\n++++++++++\nStoping Goldengate on :"+my_stack)
##    gg_update('stop',my_tenancy,my_stack)
##    response = gg_update('status',my_tenancy,my_stack)
##    while response == "STOPPING":
##      time.sleep(20)
##      response = gg_update('status',my_tenancy,my_stack)
##'''
##
##print(a)
##
##
##
##'''
##    Mani Commented this region to exclude GG from QM
##    #GG
##    print("\n++++++++++\nStoping Goldengate on :"+my_stack)
##    gg_update('stop',my_tenancy,my_stack)
##    response = gg_update('status',my_tenancy,my_stack)
##    while response == "STOPPING":
##      time.sleep(20)
##      response = gg_update('status',my_tenancy,my_stack)
##'''





import sys

def printf(x):
      print(x)
      sys.stdout.flush()

printf('abc')

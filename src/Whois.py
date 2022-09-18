import whois

def Make_consult_whois():

    domain = str(input('Domain Name: '))
    consult = whois.whois(domain)
    print(consult.email)
    print("#" * 80)
    print(consult.text)
    
    
Make_consult_whois()
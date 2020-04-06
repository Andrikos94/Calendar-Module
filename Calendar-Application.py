import calendar

#Weekheader function ->Εμφανίζει τις ημέρες της εβδομάδος με διάστημα (3) χαρακτήρων.
print(calendar.weekheader(3))
print()
#Firstweekday function ->Εμφανίζει σε integer την πρώτη ημέρα της εβδομάδας (π.χ Δευτέρα=0)
print(calendar.firstweekday())
print()
#Month function ->Εμφανίζει τον μήνα ολόκληρο απο την χρονιά που θέλουμε με διάστημα (10) χαρακτήρων
print(calendar.month(2020,4,10))
#Monthcalendar ->Εμφανίζει τον μήνα ολόκληρο σε array list
print(calendar.monthcalendar(2020,4))
#Calendar function ->Εμφανίζει ολόκληρη την χρονιά με διάστημα (2) χαρακτήρων
print(calendar.calendar(2020,2))
#Weekday function ->Εμφανίζει με βάση το έτος,τον μήνα και την ημέρα , τι ημέρα πέφτει (0=Δευτέρα,1=Τρίτη....)
today = calendar.weekday(2069,10,31)
print(today)
#Isleap function ->Εμφανίζει αν στο έτος που βάζουμε έχουμε +1 μέρα τον Φεβρουάριο (κάθε 4 χρόνια Φεβρουάριος +1 μέρα)
isleap_day=calendar.isleap(2020)
print()
print(isleap_day)
print()
#Leapdays function ->Εμφανίζει σε σύγκριση 2 ετών πόσες φορές ο Φεβρουάριος πάει (+1)
how_many_leaps_day = calendar.leapdays(2020,2040)
print(how_many_leaps_day)
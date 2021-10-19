days = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"] # All the days in the week


def all_days(days):
    work_days = "Alle dagen van de week zijn: "
    array_joined = ", ".join(days)
    work_days += array_joined + "."

    return work_days


def work_days(days):
    work_days = "De werkdagen zijn: "
    array_joined = ", ".join(days[:5])
    work_days += array_joined + "."

    return work_days



def week_days(days):
    week_days = "De weekenddagen: "
    array_joined = ", ".join(days[5:7])
    week_days += array_joined + "."

    return week_days


def all_days_back(days):
    all_days_back = "Alle dagen van de week in omgekeerde volgorde zijn: "
    array_joined = ", ".join(reversed(days))
    all_days_back += array_joined + "."

    return all_days_back

def all_days_back(days):
    all_days_back = "Alle dagen van de week in omgekeerde volgorde zijn: "
    array_joined = ", ".join(reversed(days))
    all_days_back += array_joined + "."

    return all_days_back

def work_days_back(days):
    all_days_back = "Alle dagen van de week in omgekeerde volgorde zijn: "
    array_joined = ", ".join(reversed(days[:5]))
    all_days_back += array_joined + "."

    return all_days_back

def week_days_back(days):
    all_days_back = "Alle dagen van de week in omgekeerde volgorde zijn: "
    array_joined = ", ".join(reversed(days[5:7]))
    all_days_back += array_joined + "."

    return all_days_back


print( all_days(days) )
print( work_days(days) )
print( week_days(days) )
print( all_days_back(days) )
print( work_days_back(days) )
print( week_days_back(days) )
from typing import List
import doctest


def what_should(prefer:list,preferrs_cout:dict)->list:
    max_res=[]
    for p in prefer:
        if len(max_res) ==0:
            max_res.append(p)
        elif preferrs_cout[max_res[0]]==preferrs_cout[p]:
            max_res.append(p)
        elif preferrs_cout[max_res[0]]<preferrs_cout[p]:
            max_res.clear()
            max_res.append(p)
    return max_res
def conditioned_utilitarian(total:float,subjects:List[str],
                preferences:List[List[str]]):
    """

    :param total:
    :param subjects:
    :param preferences:
    :return:
    >>> total=500
    >>> subjects = ["Security"]
    >>> prefer=[["Security"],["Security"]]
    >>> conditioned_utilitarian(total, subjects, prefer)
    Citizen 0 gives 250.0 to Security
    Citizen 1 gives 250.0 to Security
    Final budget:{'Security': 500.0}
    >>> subjects = ["Security","Economy"]
    >>> prefer=[["Security"],["Economy"]]
    >>> conditioned_utilitarian(total, subjects, prefer)
    Citizen 0 gives 250.0 to Security
    Citizen 1 gives 250.0 to Economy
    Final budget:{'Security': 250.0, 'Economy': 250.0}
    >>> prefer = [["Security","Economy"], ["Security","Economy"]]
    >>> conditioned_utilitarian(total, subjects, prefer)
    Citizen 0 gives 125.0 to Security and 125.0 to Economy
    Citizen 1 gives 125.0 to Security and 125.0 to Economy
    Final budget:{'Security': 250.0, 'Economy': 250.0}
    >>> prefer = [["Economy"], ["Security", "Economy"]]
    >>> conditioned_utilitarian(total, subjects, prefer)
    Citizen 0 gives 250.0 to Economy
    Citizen 1 gives 250.0 to Economy
    Final budget:{'Security': 0, 'Economy': 500.0}
    >>> subjects=["Security","Economy","Education","Sport"]
    >>> prefer=[["Security","Economy"],["Security","Education"],["Security","Sport"],["Economy","Education"],["Security"]]
    >>> conditioned_utilitarian(total,subjects,prefer)
    Citizen 0 gives 100.0 to Security
    Citizen 1 gives 100.0 to Security
    Citizen 2 gives 100.0 to Security
    Citizen 3 gives 50.0 to Economy and 50.0 to Education
    Citizen 4 gives 100.0 to Security
    Final budget:{'Security': 400.0, 'Economy': 50.0, 'Education': 50.0, 'Sport': 0}
    >>> prefer = [["Economy","Sport"], ["Security", "Education"], ["Security", "Sport"], ["Economy", "Education"], ["Security"]]
    >>> conditioned_utilitarian(total, subjects, prefer)
    Citizen 0 gives 50.0 to Economy and 50.0 to Sport
    Citizen 1 gives 100.0 to Security
    Citizen 2 gives 100.0 to Security
    Citizen 3 gives 50.0 to Economy and 50.0 to Education
    Citizen 4 gives 100.0 to Security
    Final budget:{'Security': 300.0, 'Economy': 100.0, 'Education': 50.0, 'Sport': 50.0}
    >>> prefer = [["Economy", "Sport"], ["Security", "Education"], ["Security", "Sport"], ["Economy", "Education"],["Security","Sport","Economy"]]
    >>> conditioned_utilitarian(total, subjects, prefer)
    Citizen 0 gives 50.0 to Economy and 50.0 to Sport
    Citizen 1 gives 100.0 to Security
    Citizen 2 gives 50.0 to Security and 50.0 to Sport
    Citizen 3 gives 100.0 to Economy
    Citizen 4 gives 33.333333333333336 to Security and 33.333333333333336 to Sport and 33.333333333333336 to Economy
    Final budget:{'Security': 183.33333333333334, 'Economy': 183.33333333333334, 'Education': 0, 'Sport': 133.33333333333334}

    """
    amount_to_voter=total/len(preferences)
    res = {s: 0 for s in subjects}
    preferrs_cout={s:0 for s in subjects}
    for p in preferences:
        for s in subjects:
            if s in p:
                preferrs_cout[s]+=1
    for i in range(len(preferences)):
        to_invest=what_should(preferences[i],preferrs_cout)
        amount_to_subject=amount_to_voter/len(to_invest)
        print(f"Citizen {i} gives ",end="")
        for j in range(len(to_invest)):
            res[to_invest[j]]+=amount_to_subject
            print(f"{amount_to_subject} to {to_invest[j]}",end="")
            if j<len(to_invest)-1:
                print(" and ",end="")
        print()
    print(f"Final budget:{res}")


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

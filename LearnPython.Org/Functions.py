# Modify this function to return a list of strings as defined above
def list_benefits(bef):
    benefits = bef.split(", ")
    return benefits

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions" % benefit

def name_the_benefits_of_functions():
    x = "More organized code, More readable code, Easier code reuse, Allowing programmers to share and connect code together"
    list_of_benefits = list_benefits(x)
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()


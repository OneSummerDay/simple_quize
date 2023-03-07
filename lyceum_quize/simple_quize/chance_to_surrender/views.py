from django.shortcuts import render

def index(request):
    def gima_chance(iterations, variants=4):
        final_chance = 100
        for i in range (iterations):
            final_chance = final_chance / variants
        if iterations > 5:
            final_chance += .2*final_chance
        return final_chance

    c = gima_chance(10, 4)

    context = {
        'chance': c,
    }
    return render(request, 'index.html', context)


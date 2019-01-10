import os
import pickle

import numpy as np
from django.shortcuts import render

from .forms import CpetForm
from .functions import create_cat


# Create your views here.
def mlcpet_calc(request):
    if request.method == 'POST':
        form = CpetForm(request.POST)
        if form.is_valid():
            # for pythonanywhere: the route has to be changed
            path = '/home/nrsmoll/Homepage/static/models'
            #path = '/home/nrsmoll/Dropbox/PyProjects/Homepage/static/models'
            logreg_path = os.path.join(path, 'logistic_classifier_20181201.pkl')
            with open(logreg_path, 'rb') as f:
                logreg = pickle.load(f)
            svc_path = os.path.join(path, 'svc_classifier_20181201.pkl')
            with open(svc_path, 'rb') as f:
                svc = pickle.load(f)
            rf_path = os.path.join(path, 'rf_classifier_20181201.pkl')
            with open(rf_path, 'rb') as f:
                rf = pickle.load(f)
            linear_path = os.path.join(path, 'linear_regression_20181201.pkl')
            with open(linear_path, 'rb') as f:
                linear = pickle.load(f)
            svr_path = os.path.join(path, 'svr_regression_20181201.pkl')
            with open(svr_path, 'rb') as f:
                svr = pickle.load(f)
            rfr_path = os.path.join(path, 'rfr_regression_20181201.pkl')
            with open(rfr_path, 'rb') as f:
                rfr = pickle.load(f)

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            age = form.cleaned_data['age']
            bmi = form.cleaned_data['bmi']
            chronotropic = form.cleaned_data['chronotropic']
            etco2 = form.cleaned_data['etco2']

            mlist = np.array([[age, bmi, etco2, chronotropic]])
            logpred = int(list(logreg.predict(mlist))[0])
            svcpred = int(list(svc.predict(mlist))[0])
            rfpred = int(list(rf.predict(mlist))[0])
            svrpred = int(list(svr.predict(mlist))[0])
            linpred = int(list(linear.predict(mlist))[0])
            rfrpred = int(list(rfr.predict(mlist))[0])
            # Anaerobic modelling
            logpredat = 1
            linpredat = 22
            svcpredat = 1
            svrpredat = 21
            rfpredat = 0
            rfrpredat = 25
            mylist = [logpred, svcpred, rfpred, logpredat, svcpredat, rfpredat]
            logpred, svcpred, rfpred, logpredat, svcpredat, rfpredat = list(map(lambda x: create_cat(x), mylist))

            context = {'firstname': firstname, 'lastname': lastname, 'age': age, 'bmi': bmi,
                       'chronotropic': chronotropic, 'etco2': etco2,
                       'vo2maxcat1': logpred, 'atcat1': logpredat,
                       'vo2maxcat2': svcpred, 'atcat2': svcpredat,
                       'vo2maxcat3': rfpred, 'atcat3': rfpredat,
                       'vo2maxest1': linpred, 'atest1': linpredat,
                       'vo2maxest2': svrpred, 'atest2': svrpredat,
                       'vo2maxest3': rfrpred, 'atest3': rfrpredat}
            return render(request, 'mlCPET_results.html', context)
    else:
        form = CpetForm()
    return render(request, 'mlCPET.html', {'form': form})

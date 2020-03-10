# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
                My data is sourced from their most recent release at the time of writing (March 7, 2020). While 
                my model is strictly for educational purposes I hope it may offer some value in helping better understand
                what type of animals find homes, since as we gain understanding we can concentrate efforts more effectively
                on the animals that are the highest risk for negative outcomes such as being harder to find homes alongside
                euthanasia and death.
                
                My dataset consists of largely categorical data of cats and dogs while it does contain entries for other 
                animals (around 5%) for this project I’m going to be focusing strictly on our canine and feline friends.
                I split my data using sklearn train_test_split holding out 15% of the dataset to test my model on. 
                I didn't leave any data for validation as I planned to use cross validation in the models.
                
                My object with this build is to look at the "Outcome Type" class. It is a multi class classification
                target that originally consisted of 8 unique values. I dropped four of the values (Died, Rto-Adopt, 
                Disposal, Missing) that were in the dataset as they accounted for less that 1.5% combined in the 
                dataset. I didn't think keeping them would produce good results with predicting later in the build. 
                My goal is to predict the probability of each of the remaining outcome types while showing through a 
                plotly app how different changes in other classes affect the probability of the Outcomes. My target's 
                classes are well distrubuted once the four low ocurring outcomes were removed.
                
                ##### Some of the notable data wrangling I performed:
                * I found that the included Age upon Outcome class was not very useful in it's original state. It consisted of imprecise 
                values (eg: 2 weeks, 5 years, 8 months, ect). What I did was take the DateTime and Date of Birth classes (both of which 
                didn't have hardly any missing values) and subtracted them producing a datatime day value, which resulted in a usable 
                Outcome Age (days) class.
                * Some of the classes combinded data that was more useful as seperate classes. For example I took the 
                Sex upon Outcome and split the data into a Sex and Spay/Neuter classes. One to show if it was male or 
                female and one to show if the animal was intact or spayed or neutered.
                * I wanted to only use certain aspects of the originals datasets "Outcome Subtype" as I felt it consisted 
                of data leakage as most of the values could only be known once the Outcome was also known. On the other 
                hand it does have values that we would know prior to the outcome such as if the animal had rabies or was 
                suffering.
                Some of the notable data cleaning I performed:
                * To try to reduce the high cardinality of color and breed classes I only kept colors and breeds that had ocurrences of 275 and 200 respectively. All other colors and breeds that couldn't meet that threshold were marked as other.
                Also in the name category there were random punctuations in the values that I removed.
                I ultimately changed the case of the entire dataset to lowercase as I didn't want to deal with values being read as different values because of case
            """
        ),
        html.Img(src='../assets/Plot1.png.', width="650", height="400"),

        dcc.Markdown(
            '''
                #### Models
                With my baseline I used a DummyClassifer and ran a for loop to test all strategies. What I found was 
                that choosing the most_frequent occurrence (Adoption) would be your best bet if you were just trying to 
                guess. You'd be right about 47% of the time not even quite 50% which in my opinion wouldn't be very useful 
                if the goal is to tackle animal homelessness effectively.
                
                `strategies = ['stratified',  'uniform', 'prior', 'most_frequent']

                for strategy in strategies:
                    baseline = DummyClassifier(strategy = strategy)
                    baseline.fit(X_train, y_train)
                
                    y_pred = baseline.predict(X_train)
                    base_score = accuracy_score(y_train, y_pred)
                    print(f'{strategy} accuracy: {base_score}\n')`
                    
                I fit a linear model to see how that would perform. I saw a 22% improvement over the baseline model, 
                which was good but I believed the model could be better. Ultimately I went with my best performing model 
                which was a gradient boosting model. I used XGBoost's library a XGBClassifier model, it predicted my 
                target with an accuracy of about 76% an almost 29% gain over the baseline model.
                
                `XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                colsample_bynode=1, colsample_bytree=1, gamma=0,
                learning_rate=0.25, max_delta_step=0, max_depth=4,
                min_child_weight=1, missing=None, n_estimators=1000, n_jobs=-1,
                nthread=None, objective='multi:softprob', random_state=0,
                reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
                silent=None, subsample=1, verbosity=1)`
                
            
                Below are the permutation importances are the features. It confirmed my thought of how much of a 
                role age plays in a animals outcome. 
            '''
        ),
        html.Img(src='../assets/eli5.png', width="225", height="475"),
        html.Img(src='../assets/OutcomeAge.png', width="320", height="300"),
        html.Img(src='../assets/Shap Sum.png', width="310", height="320"),

    ],
)

layout = dbc.Row([column1])
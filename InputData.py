POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1/52       # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

# transition matrix
RATE_MATRIX_ANTI = [
    [None,  0.0136,   0.0,    0.01931],   # Well
    [0,     None,    52.0,    0.0],   # Stroke
    [0,     0.02235,   None,   0.02429],   # Post-Stroke
    [0.0,   0.0,    0.0,    None],   # Dead
    ]
RATE_MATRIX_NONE = [
    [None,  0.0136,   0.0,    0.01931],   # Well
    [0,     None,    52.0,    0.0],   # Stroke
    [0,     0.0298,   None,   0.02526],   # Post-Stroke
    [0.0,   0.0,    0.0,    None],   # Dead
    ]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
#RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
#RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0  # dead
]

HEALTH_COST_NONE = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]


HEALTH_COST_ANTI = [
    0,
    5000,  # stroke
    750,  # post-stroke /year
    0
]

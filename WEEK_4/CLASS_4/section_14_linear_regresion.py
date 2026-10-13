# | Hours (x) | Score (y) | Mean x | Mean y | Dev x = x−x̄ | Dev y = y−ȳ | Dev x × Dev y | Dev x² |
# | --------: | --------: | -----: | -----: | -----------: | ----------: | ------------: | -----: |
# |         1 |        35 |      3 |     55 |           -2 |         -20 |            40 |      4 |
# |         2 |        40 |      3 |     55 |           -1 |         -15 |            15 |      1 |
# |         3 |        50 |      3 |     55 |            0 |          -5 |             0 |      0 |
# |         4 |        60 |      3 |     55 |            1 |           5 |             5 |      1 |
# |         5 |        70 |      3 |     55 |            2 |          15 |            30 |      4 |
# | **Total** |   **255** |        |        |        **0** |       **0** |        **90** | **10** |

#slope (m) :  {sum of (product multiplication of dev(x) * dev(y) )} / {sum of (square of dev x)} = 90/10 = 9 m can be donated with any of other alphabets too that is w = weight
#slope when y depends on mupliple values m1 = dev(z) * dev(y) )} / {sum of (square of dev z)}, m2 = dev(v) * dev(y) )} / {sum of (square of dev v)} 
#intercept formula : c = mean(y) - [m * mean(x)] -> m = slope which we find above = 55 - 9 * 3 = 55-27= 28 same for incept can be given any other alphabets too that is b , d or so on..
#intercept when y depends on multipe values :c=mean(y) c = c - [m1x + m2z + m3v + .... m(n)a] here x,z,v,a are factors that effect the price or y and u have to substract the upcoming one from c if u write a loop
#final linear regression line and prediction : y = m(x) + c 
#final linear regression line and prediction for multiple : y=c y = y + [m1x+m2z+m3v ..... m(n)a]
# lets find our for 7 hours of studies -> here x = 7 so y = 9(7) + 28 = 91


#coding in accordance of above table and information.
# ============================================================
# LINEAR REGRESSION
# ============================================================
# x = Hours studied
# y = Exam score
# ============================================================


# ------------------------------------------------------------
# 1. Our original data
# ------------------------------------------------------------

x = [1, 2, 3, 4, 5]
y = [35, 40, 50, 60, 70]


# ------------------------------------------------------------
# 2. Mean of x
# ------------------------------------------------------------
# Formula:
#
# mean(x) = sum of x / number of x values
#
# (1 + 2 + 3 + 4 + 5) / 5 = 3

mean_x = sum(x) / len(x)

print("Mean x =", mean_x)


# ------------------------------------------------------------
# 3. Mean of y
# ------------------------------------------------------------
# According to your table you are using 55.
#
# NOTE:
# Actual mean of y is:
#
# (35 + 40 + 50 + 60 + 70) / 5
# = 255 / 5
# = 51
#
# But here we use 55 because that is the value
# in your example.

mean_y = 55

print("Mean y =", mean_y)


# ------------------------------------------------------------
# 4. Create lists for our calculated columns
# ------------------------------------------------------------

dev_x = []
dev_y = []

product_dev = []

square_dev_x = []


# ------------------------------------------------------------
# 5. Calculate each row
# ------------------------------------------------------------

for i in range(len(x)):

    # --------------------------------------------------------
    # Deviation of x
    #
    # Dev x = x - mean(x)
    #
    # Example for first row:
    # 1 - 3 = -2
    # --------------------------------------------------------

    dx = x[i] - mean_x


    # --------------------------------------------------------
    # Deviation of y
    #
    # Dev y = y - mean(y)
    #
    # Example:
    # 35 - 55 = -20
    # --------------------------------------------------------

    dy = y[i] - mean_y


    # --------------------------------------------------------
    # Product of Dev x and Dev y
    #
    # Dev x × Dev y
    #
    # Example:
    # (-2) × (-20) = 40
    # --------------------------------------------------------

    product = dx * dy


    # --------------------------------------------------------
    # Square of Dev x
    #
    # Dev x²
    #
    # Example:
    # (-2)² = 4
    # --------------------------------------------------------

    square = dx ** 2


    # --------------------------------------------------------
    # Store the values in their lists
    # --------------------------------------------------------

    dev_x.append(dx)
    dev_y.append(dy)
    product_dev.append(product)
    square_dev_x.append(square)


# ------------------------------------------------------------
# 6. Print the complete table
# ------------------------------------------------------------

print("\nComplete Table")
print("-" * 100)

print(
    "x\t y\t Mean x\t Mean y\t Dev x\t Dev y\t Dev x*Dev y\t Dev x²"
)

print("-" * 100)


for i in range(len(x)):

    print(
        f"{x[i]}\t"
        f"{y[i]}\t"
        f"{mean_x}\t"
        f"{mean_y}\t"
        f"{dev_x[i]}\t"
        f"{dev_y[i]}\t"
        f"{product_dev[i]}\t\t"
        f"{square_dev_x[i]}"
    )


# ------------------------------------------------------------
# 7. Calculate totals
# ------------------------------------------------------------

sum_product = sum(product_dev)

sum_square = sum(square_dev_x)


print("-" * 100)

print(
    f"Total\t"
    f"{sum(y)}\t\t\t"
    f"{sum(dev_x)}\t"
    f"{sum(dev_y)}\t"
    f"{sum_product}\t\t"
    f"{sum_square}"
)


# ============================================================
# 8. FIND THE SLOPE (m)
# ============================================================

# Formula:
#
#              Σ(Dev x × Dev y)
# m = -------------------------------
#              Σ(Dev x²)
#
# In our example:
#
# m = 90 / 10
# m = 9

m = sum_product / sum_square


print("\nSlope (m) =", m)


# ============================================================
# 9. FIND THE INTERCEPT (c)
# ============================================================

# Formula:
#
# c = mean(y) - [m × mean(x)]
#
# c = 55 - [9 × 3]
# c = 55 - 27
# c = 28

c = mean_y - (m * mean_x)


print("Intercept (c) =", c)


# ============================================================
# 10. FINAL LINEAR REGRESSION EQUATION
# ============================================================

# Formula:
#
# y = mx + c
#
# Therefore:
#
# y = 9x + 28

print("\nLinear Regression Equation:")

print(f"y = {m}x + {c}")


# ============================================================
# 11. PREDICTION
# ============================================================

# We want to predict the score
# for 7 hours of study.

new_x = 7


# Formula:
#
# y = mx + c 
#
# y = 9(7) + 28
# y = 63 + 28
# y = 91

predicted_y = (m * new_x) + c


print("\nPrediction")
print("Hours studied =", new_x)
print("Predicted score =", predicted_y)
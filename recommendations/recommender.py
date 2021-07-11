import pandas as pd
# from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_excel(r'C:\Users\Toyosi.Toyosi-PC\PycharmProjects\srwebsite\recommendations\response to stress.xlsx',
                        index_col=0)
ratings = ratings.fillna(0)
# print(ratings)


def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row


ratings_std = ratings.apply(standardize)
# print(ratings_std)


# taking transpose to get similarity between items in the same rows
item_similarity = cosine_similarity(ratings_std.T)
# print(item_similarity)


item_similarity_df = pd.DataFrame(item_similarity, index=ratings.columns, columns=ratings.columns)
# print(item_similarity_df)


# let's make recommendations
def get_similar_stress_reduction_method(method, rating):
    similar_score = item_similarity_df[method] * (rating - 2.5)  # 2.5 is the mean of the ratings
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score
# print(get_similar_stress_reduction_method("Yoga", 4))


"""
def outer_func():
    def inner_func():
        print("Hello, World!")
    inner_func()

outer_func()
"""

selection_list = []


def get_data(method_id, method_rating):
    selection_list.append((method_id, method_rating))
    return selection_list

"""
get_data('Yoga', 4)
get_data("laughter", 4)

similar_method = pd.DataFrame()

for method, rating in selection_list:
    similar_method = similar_method.append(get_similar_stress_reduction_method(method, rating), ignore_index=True)


stress_reduction_lover = [("laughter", 4), ("Yoga", 3), ("Taking Oatmeal", 1)]

similar_method = pd.DataFrame()

for method, rating in stress_reduction_lover:
    similar_method = similar_method.append(get_similar_stress_reduction_method(method, rating), ignore_index=True)
"""

# print(similar_method.head())
def recommendation(selection_list):
    similar_method = pd.DataFrame()
    for method, rating in selection_list:
        similar_method = similar_method.append(get_similar_stress_reduction_method(method, rating), ignore_index=True)
    recommend = similar_method.sum().sort_values(ascending=False)
    return recommend


recommendation = recommendation(selection_list)
print(recommendation)

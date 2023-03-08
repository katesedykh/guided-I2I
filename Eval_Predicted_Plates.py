import os
import sys
sys.path.append('/projects/')
import pandas as pd
import numpy as np
import cv2
from PIL import Image
import os
import shutil
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from scipy.spatial.distance import cosine

from sklearn.metrics.pairwise import cosine_similarity

plate = "Actives_Plate_B"
model = "AdaGN_Pert_CG_Pert"#_unlabelled"

# Ground Truth Plate
GT_dir = f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/{plate}/Ground_Truth/"
# Predicted Plate
Predicted_dir = f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/{plate}/{model}/"
# Cellprofuler Features:
#Feature_path = f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/only_active_normalization/plateA_all_combined_normalization_featureSelect"



#Combined_standardized_featureselect_AdaGN-None_CG-None
#Combined_standardized_featureselect_AdaGN-Pert_CG-None
#Combined_standardized_featureselect_AdaGN-Pert_CG-None_unlabelled
#Combined_standardized_featureselect_AdaGN-Target_CG-None <<<<<<<<<<<<<<<<<<<<<<<<< don't have this yet, have re-run
#Combined_standardized_featureselect_AdaGN-Target_CG-None_unlabelled


#
##### TABLE 1: Image metrics ######
#
## FID
#
## run:
## python -m pytorch_fid "/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/Plate_A/Ground_Truth/" "/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/Plate_A/AdaGN-Pert_CG-None/"
#
## got 3.9552 for batch A (None_None)
## got 3.1296 for batch B (None_None)
## got 6.0277 for batch B (Batch_None)
#
##SSIM
#def SSIM_function(prediction, ground_truth):
#    return ssim(prediction, ground_truth)
#
## CorCeof
#def CorCoef_function(prediction, ground_truth):
#    a_temp = np.corrcoef(prediction.flatten(), ground_truth.flatten())
#    return a_temp[1,0]
#
## MSE/MAE
#def MSE_function(prediction, ground_truth):
#    return mean_squared_error(prediction, ground_truth)
#
#def MAE_function(prediction, ground_truth):
#    return mean_absolute_error(prediction, ground_truth)
#
#
#fileList = os.listdir(GT_dir)
#channel_list = ["C01.tiff","C02.tiff","C03.tiff","C04.tiff","C05.tiff"]
#
#corcoef_all_channels, corcoef_std_all_channels = [], []
#ssim_all_channels, ssim_std_all_channels = [], []
#mse_all_channels, mse_std_all_channels = [], []
#mae_all_channels, mae_std_all_channels = [], []
#
#for channel in channel_list:
#    print(channel)
#    corcoef_mean, corcoef_all = [], []
#    ssim_mean, ssim_all = [], []
#    mse_mean, mse_all = [], []
#    mae_mean, mae_all = [], []
#
#    for fname in fileList:
#    #    # Print the file name
#        if fname.endswith(channel):
##            print(fname) 
#            GT_path = os.path.join(GT_dir, fname)
#            Pred_path = os.path.join(Predicted_dir, fname)
#            # Open the images
#            GT_image = np.array(Image.open(GT_path))
#            Pred_image = np.array(Image.open(Pred_path))
#            
#            corcoef_hold = CorCoef_function(GT_image,Pred_image)
#            ssim_hold = SSIM_function(GT_image,Pred_image)
#            mse_hold = MSE_function(GT_image,Pred_image)
#            mae_hold = MAE_function(GT_image,Pred_image)
#
#            corcoef_all.append(corcoef_hold)
#            ssim_all.append(ssim_hold)
#            mse_all.append(mse_hold)
#            mae_all.append(mae_hold)
#
#
#    corcoef_mean = sum(corcoef_all)/len(corcoef_all)
#    ssim_mean = sum(ssim_all)/len(ssim_all)
#    mse_mean = sum(mse_all)/len(mse_all)
#    mae_mean = sum(mae_all)/len(mae_all)
#    corcoef_std = np.std(corcoef_all)
#    ssim_std = np.std(ssim_all)
#    mse_std = np.std(mse_all)
#    mae_std = np.std(mae_all)
#    
#    corcoef_all_channels.append(corcoef_mean)
#    ssim_all_channels.append(ssim_mean)
#    mse_all_channels.append(mse_mean)
#    mae_all_channels.append(mae_mean)
#    
#    corcoef_std_all_channels.append(corcoef_std)
#    ssim_std_all_channels.append(ssim_std)
#    mse_std_all_channels.append(mse_std)
#    mae_std_all_channels.append(mae_std)
#
#
#Channel_cols = ["C01", "C02", "C03", "C04", "C05"]
#
#col_df = []
#col_df.append(corcoef_all_channels)
#col_df.append(ssim_all_channels)
#col_df.append(mse_all_channels)
#col_df.append(mae_all_channels)
#
#df_metrics = pd.DataFrame(col_df, columns=Channel_cols, index = ['corcoef', 'ssim', 'mse', 'mae'])
#print(df_metrics)
#df_metrics.to_csv(f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/{plate}/metrics_{model}.csv")
#
#col_df_std = []
#col_df_std.append(corcoef_std_all_channels)
#col_df_std.append(ssim_std_all_channels)
#col_df_std.append(mse_std_all_channels)
#col_df_std.append(mae_std_all_channels)
#
#df_metrics_std = pd.DataFrame(col_df_std, columns=Channel_cols, index = ['corcoef', 'ssim', 'mse', 'mae'])
#print(df_metrics_std)
#df_metrics_std.to_csv(f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/{plate}/metrics_std_{model}.csv")
#


###### TABLE 2: Feature Evaluation ######

#Load features generated by "Process_features_with_annotations.py" script

#All_feats = pd.read_csv(f'{plate}_annotated_features_{model}_all.csv')
#Active_feats = pd.read_csv(f'{plate}_annotated_features_{model}_actives.csv')
#No_controls_feats = pd.read_csv(f'{plate}_annotated_features_{model}_no_controls.csv')
#DMSO_feats = pd.read_csv(f'{plate}_annotated_features_{model}_controls.csv')
#

# Active subeset:
#
All_feats = pd.read_csv(f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/{plate}_annotated_features_{model}_all.csv")

All_feats = All_feats[All_feats.duplicated(subset=['Metadata_broad_sample','pert_iname'], keep=False)]


#f'{plate}_annotated_features_{model}_all.csv'
#Splitter

def SplitGTandPred(feats):
    GT_All_feats = feats[~feats["Metadata_Plate"].str.contains("Pred_")]
    Pred_All_feats = feats[feats["Metadata_Plate"].str.contains("Pred_")]
    
    GT_All_feats_values = GT_All_feats.iloc[:,6:]
    GT_All_feats_values = GT_All_feats_values.reset_index(drop=True)
    Pred_All_feats_values = Pred_All_feats.iloc[:,6:]
    Pred_All_feats_values = Pred_All_feats_values.reset_index(drop=True)
    return GT_All_feats_values, Pred_All_feats_values

# Calculate Feature Correlations for all features

def Calculate_Feature_Correlation(feats):
    GT_All_feats_values, Pred_All_feats_values = SplitGTandPred(feats)
    Feature_correlations = Pred_All_feats_values.corrwith(GT_All_feats_values, axis = 0)
    return(np.mean(Feature_correlations))
    

# Calculate Mean Distance (in feature space) to matching target

def Mean_Cosine_Distance_to_matching_target(feats):
    unique_targets = feats["target"].unique()
    cosine_dists = []
    for target in unique_targets:
        target_rows = feats[feats["target"] == target]
        target_features = target_rows.drop(["Metadata_Well","Metadata_broad_sample","pert_iname","target","Metadata_Plate"], axis=1)
        target_features = target_features.reset_index(drop=True)
        target_features = target_features.iloc[:,1:]
        for i in range(target_features.shape[0]):
            f1 = target_features.iloc[i, :]
            for j in range(target_features.shape[0]):
                if i == j:
                    continue
                f2 = target_features.iloc[j, :]
                cosine_dist = cosine(f1, f2)
        cosine_dists.append(cosine_dist)
    mean_cosine_distance = np.mean(cosine_dists)
    std_cosine_distance = np.std(cosine_dists)
    return mean_cosine_distance, std_cosine_distance

# 1NN function:

def classify_1nn(df_values, df_class, index):
  min_dist = float("inf")
  test_row = df_values.iloc[index,:]
  predicted_class = None
  for i, row in df_values.iterrows():
    if i == index:
        pass
    else:
        dist = cosine(test_row, row)
        if dist < min_dist:
          min_dist = dist
          predicted_class_row = df_class.iloc[i,:]
          predicted_class = predicted_class_row["target"]
  return predicted_class

# Calculate NSC matching (Equivalent to 1NN matching for Target2)

def NSC_match_GT(feats):
      GT_All_feats = feats[~feats["Metadata_Plate"].str.contains("Pred_")]
      GT_All_feats = GT_All_feats.reset_index(drop=True)   
      GT_All_feats_values = GT_All_feats.iloc[:,6:]
      GT_All_feats_values = GT_All_feats_values.reset_index(drop=True)
      GT_All_feats["predicted_target"] = None
      for i, row in GT_All_feats_values.iterrows():
          predicted_class = classify_1nn(GT_All_feats_values, GT_All_feats, i)
          GT_All_feats.loc[i, "predicted_target"] = predicted_class
          a = GT_All_feats[["target", "predicted_target"]]
      count = 0
      for i, row in a.iterrows():
          if row["target"] == row["predicted_target"]:
              count += 1
          else:
              count += 0         
      return a, count#/len(a)
  
    
def NSC_match_Pred(feats):
      Pred_All_feats = feats[feats["Metadata_Plate"].str.contains("Pred_")]
      Pred_All_feats = Pred_All_feats.reset_index(drop=True)
      Pred_All_feats_values = Pred_All_feats.iloc[:,6:]
      Pred_All_feats_values = Pred_All_feats_values.reset_index(drop=True)
      Pred_All_feats["predicted_target"] = None
      for i, row in Pred_All_feats_values.iterrows():
          predicted_class = classify_1nn(Pred_All_feats_values, Pred_All_feats, i)
          Pred_All_feats.loc[i, "predicted_target"] = predicted_class
          a = Pred_All_feats[["target", "predicted_target"]]          
      count = 0
      for i, row in a.iterrows():
          if row["target"] == row["predicted_target"]:
              count += 1
          else:
              count += 0
      return a, count#/len(a)
  
    
def top5_NSC_match_Pred(feats):
      Pred_All_feats = feats[~feats["Metadata_Plate"].str.contains("Pred_")]
      Pred_All_feats = Pred_All_feats.reset_index(drop=True)
      Pred_All_feats_values = Pred_All_feats.iloc[:,6:]
      Pred_All_feats_values = Pred_All_feats_values.reset_index(drop=True)
      Pred_All_feats["predicted_target"] = None
      
      list_of_top_5 = find_nearest_neighbors(Pred_All_feats_values, n=5)
#      print(list_of_top_5)
      count = 0
      for i, row in Pred_All_feats_values.iterrows():
#          print(i)
          indexes = list_of_top_5[i]
          orig_target = Pred_All_feats.iloc[i,:]
          orig_target = orig_target["target"]
          for j in indexes:
              
#              print(j)
              a_temp = Pred_All_feats.iloc[j,:]
              pred_target = a_temp["target"]
              if orig_target == pred_target:
                  count += 1
              else:
                  count += 0
#          predicted_class = #classify_1nn(Pred_All_feats_values, Pred_All_feats, i)
#          Pred_All_feats.loc[i, "predicted_target"] = predicted_class
#          a = Pred_All_feats[["target", "predicted_target"]]      
      
#      count = 0
#      for i, row in a.iterrows():
#          if row["target"] == row["predicted_target"]:
#              count += 1
#          else:
#              count += 0
      return count#/len(a)


def find_nearest_neighbors(df, n=5):
    cosine_similarities = cosine_similarity(df)
    nearest_neighbors = []
    for i in range(len(cosine_similarities)):
        closest = cosine_similarities[i].argsort()[-n-1:-1][::-1]
        nearest_neighbors.append(closest)
    return nearest_neighbors


# Praveen Metric:search GT space for a match using the predicted actives (only)
#	- praveen wants list of wells which match to ground truth
#	- he can make a list of matching bioloigcal pairs.

def classify_1nn_Praveen(df_values, GT_values, df_class, index):
  min_dist = float("inf")
  test_row = df_values.iloc[index,:]
  predicted_class = None
  for i, row in GT_values.iterrows():
    if i == index:
        pass
    else:
        dist = cosine(test_row, row)
        if dist < min_dist:
          min_dist = dist
          predicted_class_row = df_class.iloc[i,:]
          predicted_class = predicted_class_row["target"]
  return predicted_class


def Praveen_Function(feats):
    GT_All_feats = feats[~feats["Metadata_Plate"].str.contains("Pred_")]
    GT_All_feats = GT_All_feats.reset_index(drop=True)
    GT_All_feats_values = GT_All_feats.iloc[:,6:]
    GT_All_feats_values = GT_All_feats_values.reset_index(drop=True)
    Pred_All_feats = feats[feats["Metadata_Plate"].str.contains("Pred_")]
    Pred_All_feats = Pred_All_feats.reset_index(drop=True)
    Pred_All_feats_values = Pred_All_feats.iloc[:,6:]
    Pred_All_feats_values = Pred_All_feats_values.reset_index(drop=True)
    
    Pred_All_feats["predicted_target"] = None
    for i, row in Pred_All_feats_values.iterrows():
          predicted_class = classify_1nn_Praveen(Pred_All_feats_values, GT_All_feats_values, Pred_All_feats, i)
          Pred_All_feats.loc[i, "predicted_target"] = predicted_class
          a = Pred_All_feats[["target", "predicted_target"]]          
    count = 0
    for i, row in a.iterrows():
          if row["target"] == row["predicted_target"]:
              count += 1
          else:
              count += 0
    return a, count#/len(a)

#
#test_feature = All_feats # All_feats
#
#print("Mean feature correlation between pred and GT")
#print(Calculate_Feature_Correlation(test_feature))
#
#GT_All_feats = test_feature[~test_feature["Metadata_Plate"].str.contains("Pred_")]
#Pred_All_feats = test_feature[test_feature["Metadata_Plate"].str.contains("Pred_")]
#
#print("GT mean dist to matching target")
#print(Mean_Cosine_Distance_to_matching_target(GT_All_feats))
#
#print("Prediction mean dist to matching target")
#print(Mean_Cosine_Distance_to_matching_target(Pred_All_feats))
#
#print('top 5')
#print(top5_NSC_match_Pred(test_feature))
#
#print('1NN gt vs pred')
#print(NSC_match_GT(test_feature))
#print(NSC_match_Pred(test_feature))
#

#print('std of data')
#print()


##print(Praveen_Function(Active_feats))
#
######## Appendix: ######
#
#
## Create Feature Correlation Matrix
#
#
#
#
#
#
#plate = "Actives_Plate_B"
#model = "AdaGN_Pert_CG_Pert"#_unlabelled"
#
## Ground Truth Plate
#GT_dir = f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/{plate}/Ground_Truth/"
## Predicted Plate
#Predicted_dir = f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/Actives_Plate_B/{model}/"
#
#
#All_feats = pd.read_csv(f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/{plate}_annotated_features_{model}_all.csv")
#
#All_feats = All_feats[All_feats.duplicated(subset=['Metadata_broad_sample','pert_iname'], keep=False)]




## This calculates the correlation between the shared selected features in plates A and B (GT)
## We can also calculate the correlation between predicted A and predicted B (two completely different models to compare reproducibility

GT_all_A = pd.read_csv(f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/Actives_Plate_A_annotated_features_{model}_all.csv")
GT_all_B = pd.read_csv(f"/projects/img/GAN_CP/PAPER_3/Palette-Image-to-Image-Diffusion-Models-main/Actives_Plate_B_annotated_features_{model}_all.csv")

GT_All_feats_A = GT_all_A[~GT_all_A["Metadata_Plate"].str.contains("Pred_")]
GT_All_feats_B = GT_all_B[~GT_all_B["Metadata_Plate"].str.contains("Pred_")]

GT_All_feats_A = GT_All_feats_A.iloc[:,5:]
GT_All_feats_A = GT_All_feats_A.reset_index(drop=True)
GT_All_feats_B = GT_All_feats_B.iloc[:,5:]
GT_All_feats_B = GT_All_feats_B.reset_index(drop=True)


a = np.intersect1d(GT_All_feats_A.columns, GT_All_feats_B.columns)
#a = np.delete(a,['Metadata_broad_sample', 'Metadata_Well', 'Metadata_concentration'])
print(len(a))

ab = GT_All_feats_A[a].corrwith(GT_All_feats_B[a], axis = 0)
print(np.mean(ab))


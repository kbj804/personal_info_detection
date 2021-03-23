#%%
from Scripts.tp.personal_information.generateData import GenerateData
from Scripts.tp.ml.h2o_helper import H2oClass

#%%
g = GenerateData()
gdf = g.file_to_dataframe(r"D:\\Project\\tesseract\\pdf_sample2.pdf")

#%%
m = H2oClass()
model = m.load_model(r"D:\\model\\GBM_1_AutoML_20210323_104837")

# %%
hdf = m.df_to_hf(gdf)
# %%
preds = model.predict(hdf)
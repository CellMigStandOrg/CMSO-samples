The idea:

The idea is to enable researchers and institutes  to select the algorithms that suit their microscopic 2D image datasets from a set of robust segmentation and tracking algorithms to tackle different challenges posite by different datasets. Among these challengs are cell deformation (division and expanding), the complexity of the cell motions, the constant changes of the cell morphology, and the removal of noisy and artifacts particles. The toolbox yet is not fully complete. We aim to optimize the tracking and the segmentation algorithms in order to capture the morphological aspects of the cell. The morphological aspects can be used to inform us plenty of information such as the behavior of the cells and why such cells move in certains ways. This feature is particularly important if one wants to do clinical analysis and infer some useful information.

About the toolbox. 

The toolbox currently has four efficient and rigorous segmentation algorithms and three tracking algorithms. The input is a time-lapsed image sequence file in any of these formats (avi, mp4,tiff, gif). The users can apply any of the segmentation algorithms to preview how each algorithms behaves and able to detect cells in the images. In general, these algorithms are able to deal with many image challenges such cell deformation and occlusion, differentiation of potential cells from noisy ones. 

The tracking algorithms are motion-based, appearance-based, and data-association based.  These algorithms output the displacement of the cells and write the trajectories into an excel file (an example of the files are in the subfolders).




The structure of the subfolders is as follows:

Under Essen folder, we apply three different algorithms (i.e, exp_1,exp_2,exp_3) on the same datafile. The results of are in the folders.

Under UGent folder, we apply one segmentation and tracking algorithm. 


Note that the toolbox is currently under development. 
-

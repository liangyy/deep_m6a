## Goal 

Build predictive model on m6a mark.

## Structure

* Codes are at `code/`
* Documentations are at `docs/` (rmarkdowns are at `rmd/`)
* Data are at `data/`
* Analysis modules are at `analysis/`

## Pipeline

The very raw data is in BED12 format. The major output should be predictive model. Besides the function for building the model based on the data, there should be a collection of functions that ensures various analyses to measure the performance and to present how model works. The following lists the pipeline and functions to be implemented (but not limited to).

* Pipeline

	- [x] Annotate every row (signal/peak) BED12 file with corresponding transcript type (5'UTR/coding region/3'UTR).  
	- [ ] Construct negative peak set with the matched transcript types.  **This is not urgent**
	- [ ] Extend/Shrink the peak according to window size setup.
	- [ ] Extract sequence from window.
	- [ ] Build model

* Function
	
	- [ ] Predict
	- [ ] Compare different peak set (size? fraction of overlap?)


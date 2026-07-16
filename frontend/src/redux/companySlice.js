import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { fetchCompany } from "../services/companyApi";

export const loadCompany = createAsyncThunk(
  "company/loadCompany",
  async (companyId) => {
    return await fetchCompany(companyId);
  }
);

const companySlice = createSlice({
  name: "company",
  initialState: {
    companies: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(loadCompany.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(loadCompany.fulfilled, (state, action) => {
        state.loading = false;
        state.companies = [action.payload];
      })
      .addCase(loadCompany.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export default companySlice.reducer;

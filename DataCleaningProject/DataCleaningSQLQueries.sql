-- Cleaning Data in SQL Queries

select *
from PortfolioProjects..NashvilleHousing


-- Standardize Date format
select SaleDateConverted, CONVERT(Date, SaleDate)
from PortfolioProjects..NashvilleHousing

alter table PortfolioProjects..NashvilleHousing
Add SaleDateConverted Date

update PortfolioProjects..NashvilleHousing
set SaleDateConverted = CONVERT(Date, SaleDate)

-- Populate property address data

select *
from PortfolioProjects..NashvilleHousing
--where PropertyAddress is null
order by ParcelID

select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
from PortfolioProjects..NashvilleHousing a
join PortfolioProjects..NashvilleHousing b
on a.ParcelID = b.ParcelID
and a.[UniqueID ] <> b.[UniqueID ]
where a.PropertyAddress is null

update a
set PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
from PortfolioProjects..NashvilleHousing a
join PortfolioProjects..NashvilleHousing b
on a.ParcelID = b.ParcelID
and a.[UniqueID ] <> b.[UniqueID ]
where a.PropertyAddress is null


-- Breaking out address into individual column(Address, City, State)

select PropertyAddress
from PortfolioProjects..NashvilleHousing


select
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) as Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) -1, LEN(PropertyAddress)) as Address

from PortfolioProjects..NashvilleHousing


alter table PortfolioProjects..NashvilleHousing
Add PropertySplitAddress Nvarchar(255)

update PortfolioProjects..NashvilleHousing
set PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)

alter table PortfolioProjects..NashvilleHousing
Add PropertySplitCity Nvarchar(255)

update PortfolioProjects..NashvilleHousing
set PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) -1, LEN(PropertyAddress))


select *
from PortfolioProjects..NashvilleHousing


select OwnerAddress
from PortfolioProjects..NashvilleHousing

Select
PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)
From PortfolioProjects..NashvilleHousing

alter table PortfolioProjects..NashvilleHousing
Add OwnerSplitAddress Nvarchar(255)

update PortfolioProjects..NashvilleHousing
set OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)

alter table PortfolioProjects..NashvilleHousing
Add OwnerSplitCity Nvarchar(255)

update PortfolioProjects..NashvilleHousing
set OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)

alter table PortfolioProjects..NashvilleHousing
Add OwnerSplitState Nvarchar(255)

update PortfolioProjects..NashvilleHousing
set OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)

select *
from PortfolioProjects..NashvilleHousing


-- Change Y and N to Yes and No in "SoldAsVacant" field

select distinct(SoldAsVacant), COUNT(SoldAsVacant)
from PortfolioProjects..NashvilleHousing
group by SoldAsVacant
order by 2


select SoldAsVacant,
case when SoldAsVacant = 'Y' then 'Yes'
when SoldAsVacant = 'N' then 'No'
else SoldAsVacant
end
from PortfolioProjects..NashvilleHousing


update PortfolioProjects..NashvilleHousing
set  SoldAsVacant = case when SoldAsVacant = 'Y' then 'Yes'
when SoldAsVacant = 'N' then 'No'
else SoldAsVacant
end



--Remove duplicate

WITH RowNumCTE AS(
Select *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
				 PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY
					UniqueID
					) row_num

From PortfolioProjects..NashvilleHousing
--order by ParcelID
)
select *
From RowNumCTE
Where row_num > 1
Order by PropertyAddress



-- Delete unused columns


select *
from PortfolioProjects..NashvilleHousing

ALTER TABLE PortfolioProjects..NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate
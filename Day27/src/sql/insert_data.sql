
INSERT INTO CS_ForeignHoldingSt 
(ID, InnerCode, TradingDay, ForeignHoldings, ForeignHoldProp, UpdateTime, InsertTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO CS_HKStockPerformance 
(ID, InnerCode, TradingDay, PrevClosePrice, OpenPrice, HighPrice, LowPrice, ClosePrice, CurrencyUnitCode, TurnoverVolume, TurnoverValue, ChangeOF, ChangePCT, RangePCT, TurnoverRate, AvgPrice, TotalMV, NegotiableMV, TurnoverValueRW, TurnoverVolumeRW, ChangeOFRW, ChangePCTRW, RangePCTRW, TurnoverRateRW, AvgPriceRW, HighPriceRW, LowPriceRW, HighestClosePriceRW, LowestClosePriceRW, TurnoverValuePerDayRW, TurnoverRatePerDayRW, TurnVolumePerDayRW, ChangePCTPerDayRW, RangePCTPerDayRW, TotalMVPerDayRW, NegotiableMVPerDayRW, TurnoverValueTW, TurnoverVolumeTW, ChangeOFTW, ChangePCTTW, RangePCTTW, TurnoverRateTW, AvgPriceTW, HighPriceTW, LowPriceTW, HighestClosePriceTW, LowestClosePriceTW, TurnoverValuePerDayTW, TurnoverRatePerDayTW, TurnVolumePerDayTW, ChangePCTPerDayTW, RangePCTPerDayTW, TotalMVPerDayTW, NegotiableMVPerDayTW, TurnoverValueRM, TurnoverVolumeRM, ChangeOFRM, ChangePCTRM, RangePCTRM, TurnoverRateRM, AvgPriceRM, HighPriceRM, LowPriceRM, HighestClosePriceRM, LowestClosePriceRM, TurnoverValuePerDayRM, TurnoverRatePerDayRM, TurnVolumePerDayRM, ChangePCTPerDayRM, RangePCTPerDayRM, TotalMVPerDayRM, NegotiableMVPerDayRM, TurnoverValueTM, TurnoverVolumeTM, ChangeOFTM, ChangePCTTM, RangePCTTM, TurnoverRateTM, AvgPriceTM, HighPriceTM, LowPriceTM, HighestClosePriceTM, LowestClosePriceTM, TurnoverValuePerDayTM, TurnoverRatePerDayTM, TurnVolumePerDayTM, ChangePCTPerDayTM, RangePCTPerDayTM, TotalMVPerDayTM, NegotiableMVPerDayTM, TurnoverValueRMThree, TurnoverVolumeRMThree, ChangeOFRMThree, ChangePCTRMThree, RangePCTRMThree, TurnoverRateRMThree, AvgPriceRMThree, HighPriceRMThree, LowPriceRMThree, HighestClosePRMThree, LowestClosePRMThree, TurnValuePDayRMThree, TurnRatePDayRMThree, TurnVolumePDayRMThree, ChangePCTPDayRMThree, RangePCTPDayRMThree, TotalMVPerDayRMThree, NegotiableMVPRMThree, TurnoverValueRMSix, TurnoverVolumeRMSix, ChangeOFRMSix, ChangePCTRMSix, RangePCTRMSix, TurnoverRateRMSix, AvgPriceRMSix, HighPriceRMSix, LowPriceRMSix, HighestClosePRMSix, LowestClosePRMSix, TurnValuePDayRMSix, TurnRatePDayRMSix, TurnVolumePDayRMSix, ChangePCTPDayRMSix, RangePCTPDayRMSix, TotalMVPerDayRMSix, NegotiableMVPRMSix, TurnoverValueRY, TurnoverVolumeRY, ChangeOFRY, ChangePCTRY, RangePCTRY, TurnoverRateRY, AvgPriceRY, HighPriceRY, LowPriceRY, HighestClosePRY, LowestClosePRY, TurnoverValuePDayRY, TurnoverRatePDayRY, TurnVolumePDayRY, ChangePCTPDayRY, RangePCTPDayRY, TotalMVPerDayRY, NegotiableMVPRY, TurnoverValueYTD, TurnoverVolumeYTD, ChangeOFYTD, ChangePCTYTD, RangePCTYTD, TurnoverRateYTD, AvgPriceYTD, HighPriceYTD, LowPriceYTD, HighestClosePriceYTD, LowestClosePriceYTD, TurnoverValuePerDayYTD, TurnoverRatePerDayYTD, TurnVolumePDayYTD, ChangePCTPerDayYTD, RangePCTPerDayYTD, TotalMVPerDayYTD, NegotiableMVPYTD, HighAdjustedPrice, HighAdjustedPriceDate, LowAdjustedPrice, LowAdjustedPriceDate, UpdateTime, InsertTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO CS_StockCapFlowIndex 
(ID, InnerCode, TradingDay, TimeRange, SmallBuyValue, SmallSellValue, SmallBuyVolume, SmallSellVolume, SmallBuyNum, SmallSellNum, SmallNetBuyValue, SmallNetBuyVolume, SmallBValueRatio, SmallSValueRatio, SmallBVolumeRatio, SmallSVolumeRatio, SmallNBValueRatio, SmallNBVFloatMVRatio, SmallNBVolumeRatio, SmallNBVFloatSRatio, SmallActBuyValue, SmallActSellValue, SmallActBuyVolume, SmallActSellVolume, SmallActBuyNum, SmallActSellNum, SmallNetActBuyValue, SmallNetActBuyVolume, SmallABValueRatio, SmallASValueRatio, SmallABVolumeRatio, SmallASVolumeRatio, SmallNABValueRatio, SmallNABVFloatMVRatio, SmallNABVolumeRatio, SmallNABVFloatSRatio, MediumBuyValue, MediumSellValue, MediumBuyVolume, MediumSellVolume, MediumBuyNum, MediumSellNum, MediumNetBuyValue, MediumNetBuyVolume, MediumBValueRatio, MediumSValueRatio, MediumBVolumeRatio, MediumSVolumeRatio, MediumNBValueRatio, MediumNBVFloatMVRatio, MediumNBVolumeRatio, MediumNBVFloatSRatio, MediumActBuyValue, MediumActSellValue, MediumActBuyVolume, MediumActSellVolume, MediumActBuyNum, MediumActSellNum, MediumNetActBuyValue, MediumNetActBuyVolume, MediumABValueRatio, MediumASValueRatio, MediumABVolumeRatio, MediumASVolumeRatio, MediumNABValueRatio, MediumNABVFloatMVRatio, MediumNABVolumeRatio, MediumNABVFloatSRatio, LargeBuyValue, LargeSellValue, LargeBuyVolume, LargeSellVolume, LargeBuyNum, LargeSellNum, LargeNetBuyValue, LargeNetBuyVolume, LargeBValueRatio, LargeSValueRatio, LargeBVolumeRatio, LargeSVolumeRatio, LargeNBValueRatio, LargeNBVFloatMVRatio, LargeNBVolumeRatio, LargeNBVFloatSRatio, LargeActBuyValue, LargeActSellValue, LargeActBuyVolume, LargeActSellVolume, LargeActBuyNum, LargeActSellNum, LargeNetActBuyValue, LargeNetActBuyVolume, LargeABValueRatio, LargeASValueRatio, LargeABVolumeRatio, LargeASVolumeRatio, LargeNABValueRatio, LargeNABVFloatMVRatio, LargeNABVolumeRatio, LargeNABVFloatSRatio, HugeBuyValue, HugeSellValue, HugeBuyVolume, HugeSellVolume, HugeBuyNum, HugeSellNum, HugeNetBuyValue, HugeNetBuyVolume, HugeBValueRatio, HugeSValueRatio, HugeBVolumeRatio, HugeSVolumeRatio, HugeNBValueRatio, HugeNBVFloatMVRatio, HugeNBVolumeRatio, HugeNBVFloatSRatio, HugeActBuyValue, HugeActSellValue, HugeActBuyVolume, HugeActSellVolume, HugeActBuyNum, HugeActSellNum, HugeNetActBuyValue, HugeNetActBuyVolume, HugeABValueRatio, HugeASValueRatio, HugeABVolumeRatio, HugeASVolumeRatio, HugeNABValueRatio, HugeNABVFloatMVRatio, HugeNABVolumeRatio, HugeNABVFloatSRatio, MainBuyValue, MainSellValue, MainBuyVolume, MainSellVolume, MainBuyNum, MainSellNum, MainNetBuyValue, MainNetBuyVolume, MainBValueRatio, MainSValueRatio, MainBVolumeRatio, MainSVolumeRatio, MainNBValueRatio, MainNBVFloatMVRatio, MainNBVolumeRatio, MainNBVFloatSRatio, MainActBuyValue, MainActSellValue, MainActBuyVolume, MainActSellVolume, MainActBuyNum, MainActSellNum, MainNetActBuyValue, MainNetActBuyVolume, MainABValueRatio, MainASValueRatio, MainABVolumeRatio, MainASVolumeRatio, MainNABValueRatio, MainNABVFloatMVRatio, MainNABVolumeRatio, MainNABVFloatSRatio, TotalBuyValue, TotalSellValue, TotalBuyVolume, TotalSellVolume, TotalBuyNum, TotalSellNum, TotalNetBuyValue, TotalNetBuyVolume, TotalBValueRatio, TotalSValueRatio, TotalBVolumeRatio, TotalSVolumeRatio, TotalNBValueRatio, TotalNBVFloatMVRatio, TotalNBVolumeRatio, TotalNBVFloatSRatio, TotalActBuyValue, TotalActSellValue, TotalActBuyVolume, TotalActSellVolume, TotalActBuyNum, TotalActSellNum, TotalNetActBuyValue, TotalNetActBuyVolume, TotalABValueRatio, TotalASValueRatio, TotalABVolumeRatio, TotalASVolumeRatio, TotalNABValueRatio, TotalNABVFloatMVRatio, TotalNABVolumeRatio, TotalNABVFloatSRatio, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO CS_StockPatterns 
(ID, InnerCode, TradingDay, GilCode, SecuMarket, IfHighestHPriceRW, IfHighestHPriceRM, IfHighestHPriceRMThree, IfHighestHPriceRMSix, IfHighestHPriceRY, IfHighestHPriceSL, IfHighestCPriceRW, IfHighestCPriceRM, IfHighestCPriceRMThree, IfHighestCPriceRMSix, IfHighestCPriceRY, IfHighestCPriceSL, IfHighestTVolumeRW, IfHighestTVolumeRM, IfHighestTVRMThree, IfHighestTVolumeRMSix, IfHighestTVolumeRY, IfHighestTVolumeSL, IfHighestTValueRW, IfHighestTValueRM, IfHighestTValueRMThree, IfHighestTValueRMSix, IfHighestTValueRY, IfHighestTValueSL, HighestHPTimesSL, HighestHPTimesRW, HighestHPTimesRM, HighestHPTimesRMThree, HighestHPTimesRMSix, HighestHPTimesRY, IfLowestLPriceRW, IfLowestLPriceRM, IfLowestLPRMThree, IfLowestLPriceRMSix, IfLowestLPriceRY, IfLowestLPriceSL, IfLowestClosePriceRW, IfLowestClosePriceRM, IfLowestCPriceRMThree, IfLowestCPriceRMSix, IfLowestClosePriceRY, IfLowestClosePriceSL, IfLowestTVolumeRW, IfLowestTVolumeRM, IfLowestTVolumeRMThree, IfLowestVolumeRMSix, IfLowestTVolumeRY, IfLowestTVolumeSL, IfLowestTValueRW, IfLowestTValueRM, IfLowestTValueRMThree, IfLowestTValueRMSix, IfLowestTValueRY, IfLowestTValueSL, LowestLowPriceTimesSL, LowestLowPriceTimesRW, LowestLowPriceTimesRM, LowestLPTimesRMThree, LowestLPTimesRMSix, LowestLPTimesRY, RisingUpDays, FallingDownDays, VolumeRisingUpDays, VolumeFallingDownDays, BreakingMAverageFive, BreakingMAverageTen, BreakingMAverageTwenty, BreakingMAverageSixty, RaisingLimitInNDays, MAverageArrangements, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO CS_TurnoverVolTecIndex 
(ID, InnerCode, GilCode, TradingDay, IndexCycle, SecuMarket, AMA5, AMA10, AMA20, AMA30, AMA60, AMA120, AMA250, VMA5, VMA10, VMA20, VMA30, VMA60, VMA120, VMA250, VMACD_EMA12, VMACD_EMA26, VMACD_DIFF, VMACD_DEA, VMACD_MACD, VolumeRatio, VOSC, TAPI_TAPI, TAPI_TAPIMA, VSTD, VROC, VR, VRSI, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO CT_SystemConst 
(ID, LB, LBMC, MS, DM, XGRQ, JSID, FVALUE, IVALUE, DVALUE, CVALUE, ID, LB, LBMC, MS, DM, XGRQ, JSID, FVALUE, IVALUE, DVALUE, CVALUE) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO HK_EmployeeChange 
(ID, InnerCode, InfoPublDate, InfoSource, SMAnnounceDate, IfEffected, EffectiveDate, QuaBeforeChange, QuaAfterChange, ExpiryDate, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO HK_SecuMain 
(ID, InnerCode, CompanyCode, SecuCode, ChiName, ChiNameAbbr, EngName, EngNameAbbr, SecuAbbr, ChiSpelling, SecuMarket, SecuCategory, ListedDate, ListedSector, ListedState, FormerName, DelistingDate, TradingUnit, TraCurrUnit, ISIN, InsertTime, XGRQ, JSID, ID, InnerCode, CompanyCode, SecuCode, ChiName, ChiNameAbbr, EngName, EngNameAbbr, SecuAbbr, ChiSpelling, SecuMarket, SecuCategory, ListedDate, ListedSector, ListedState, FormerName, DelistingDate, TradingUnit, TraCurrUnit, ISIN, InsertTime, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO HK_StockArchives 
(ID, CompanyCode, EstablishmentDate, RegAbbr, Business, InduCHKE, InduCHS, Chairman, CompanySecretary, CertifiedAccountant, RegisteredOffice, GeneralOffice, Registrars, Tel, Fax, Eail, Website, BriefIntroduction, XGRQ, JSID, CompanyType, CompanyTypeDesc, ChiName, AuditInstitution, RegCapital, RegCapitalCurrency) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_A 
(nan) 
VALUES 
(%s);


INSERT INTO LC_ASharePlacement 
(ID, InnerCode, InitialInfoPublDate, PlaYear, StockType, AdvanceDate, SMDeciPublDate, PricingModel, PricingDescription, AdvanceValidStartDate, AdvanceValidEndDate, PlaRatioPlanned, PlaPriceCeiling, PlaPriceFloor, DeciPublDate, PlaProspectusPublDate, PlaAbbrName, PlaCode, BaseShares, PlannedPlaVol, ActualPlaRatio, ActualPlaVol, PlaObject, ParValue, PlaPrice, TransferPlaRatio, TransferPlaVol, TransferFeePerShare, OddLotsTreatment, PlaProceeds, PlaCost, UnderwritingFee, CPAFee, AssetAppraisalFee, LandEvaluationFee, AttorneyFee, TotalAgentFee, OnlineIssueFee, ScripFee, SponsorFee, OtherFee, PlaNetProceeds, RightRegDate, ExRightDate, PayStartDate, PayEndDate, DateToAccount, MoneyToAccount, PlaListDate, LargeSHSubsStatement, SchemeChange, ChangeStatement, UnderwritingMode, UnderwriterBoughtVol, PublicSHSubscriptionEsti, PublicSHSubscriptionActu, XGRQ, JSID, PlannedPlaProceeds, AdjustedPlaRatioPl, AdjustedPlaVolPl, UWSponFee, CPAAppraisalFee, CSRCIACApprovalDate, SASACApprovalPublDate, CSRCApprovalPublDate, ExApprovalPublDate, IssueMethod, EventProcedureCode, LatestInfoPublDate, PlaProspectus, ResultPulbDate, ListAnnounceDate, PlannedBaseShares, PlaObjectCategory, PlaBaseDate, LargeSHHoldSum, LargeSHSubscripEsti, LargeSHSubscripActu, NAPSAfterAllotment, EPSAfterAllotment, InsertTime) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_AShareSeasonedNewIssue 
(ID, InnerCode, InitialInfoPublDate, AdvanceDate, SMDeciPublDate, AdvanceValidStartDate, AdvanceValidEndDate, IntentLetterPublDate, ProspectusPublDate, StockType, PriceIntervalStatement, PricingModel, RationModel, IssueMethod, IssueObject, IssuePriceCeiling, IssuePriceFloor, ReferringPrice, IssueVolCeiling, IssueVolFloor, OverAllotmentOption, IssueStartDate, IssueEndDate, UnderwritingStartDate, UnderwritingEndDate, IfExRightAShare, RightRegDate, ExRightDate, SuspendStartDate, SuspendEndDate, PrefPlaDateH, PrefPlaRatioH, PrefPlaApplyCodeH, PrefPlaApplyAbbrNameH, IssueDateOnline, ApplyCodeOnline, ApplyAbbrNameOnline, ApplyUnitOnline, ApplyMaxOnline, ApplyStartDateLPOffline, ApplyEndDateLPOffline, PayStartDateLPOffline, PlaPayEndDateLPOffline, ApplyUnitLPOffline, ApplyMinLPOffline, ApplyMaxLPOffline, ValidApplyTimesLPOffline, ApplyStartDateF, ApplyEndDateF, PayStartDateF, PayEndDateF, PrefAllotmentF, PrefAllotmentSingleF, STAQNETPlaStartDate, STAQNETPlaEndDate, STAQNETPlaRatio, QuotationUnitOnline, QuotationUnitOffline, OddLotsTreatment, ParValue, IssuePrice, StateSharesIssuePrice, WeightedPERatio, DilutedPERatio, IssueVol, StateSharesIssued, TotalIssueMV, IssueCost, UnderwritingFee, CPAFee, AssetAppraisalFee, LandEvaluationFee, AttorneyFee, TotalAgentFee, OnlineIssueFee, ScripFee, SponsorFee, OtherFee, IssueCostPerShare, FreezedMoney, SNIProceeds, SNINetProceeds, StateSharesProceeds, StateSharesNetProceeds, MoneyToAccount, DateToAccount, NewShareListDate, OutstandingShares, PutBackVol, PrefPlaVolH, PublicOfferVolOnline, ValidApplyVolOnline, ValidApplyNumOnline, OverSubsTimesOnline, LotRateOnline, PlaVolLPOffline, ValidApplyVolLPOffline, ValidApplyNumLPOffline, OverSubsTimesLPOffline, LotRateLPOffline, PlaVolF, PlaVolSTAQNET, TailoredPlaVolLP, EarningForecastYear, MainIncomeForecast, NetProfitForecast, DilutedEPSForecast, UnderwritingMode, UnderwriterBoughtVol, ChangeStatement, ChangeType, XGRQ, JSID, PERatioBeforeIssue, PERatioAfterIssue, PrefPlaVolHMax, PrefPlaVolHOnline, PrefPlaVolHOffline, ValidApplyHNum, ValidApplyNumHOnline, ValidApplyNumHOffline, APlaVolLPOffline, AValidApplyVolLPOffline, AValidApplyNumLPOffline, ALotRateLPOffline, BPlaVolLPOffline, BValidApplyVolLPOffline, BValidApplyNumLPOffline, BLotRateLPOffline, PlaVolHOffline, ValidPlaVolHOffline, ValidPlaNumHOffline, LotRateHOffline, SASACApprovalPublDate, CSRCApprovalPublDate, EventProcedureCode, ISOBTypeCode, AdjustedIssuePrice, PriceAdjustedDate, SchemeChangePublDate, ListAnnounceDate, ProjInfoSource, IssueResultInfoSource, AdjustedIssueVol, PriceVolAdjustedDate, IssuePurpose, PricingBaseDate, PricingBaseDateDesc, IssueType, IfEffected, SubscribeMethod, LargeSHSubMethod, LargeSHSubsSum, LargeSHSubsRatio, PlannedProceeds, CurrencyProceeds, NonCurrencyProceeds, AssetProceeds, DebtProceeds, UWSponFee, CPAAppraisalFee, ParValueCurrencyUnit, AdjustedVolFloor, AdjustedPriceCeiling, DiscountRatePerShare, SubscriptionOfferDate, OrgPriceBasePRatio, ActPriceBasePRatio, AddSubscriptionSDate, AddSubscriptionEDate, VerificationDate, LatestAdvanceDate, IfSummaryProcedure, InsertTime) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ActualController 
(ID, CompanyCode, InfoPublDate, EndDate, ControllerCode, ControllerName, EconomicNature, NationalityCode, NationalityDesc, PermanentResidency, UpdateTime, JSID, ControllerNature) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_AreaCode 
(FirstLevelCode, SecondLevelCode, AreaChiName, AreaEngName, AreaEngNameAbbr, ParentNode, ParentName, IfEffected, CancelDate, ChangeNote, Remark, InsertTime, UpdateTime, JSID, ID, AreaInnerCode) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_AuditOpinion 
(ID, CompanyCode, EndDate, InfoSource, AccountingFirms, InstiBelongedCode, CPA, OpinionType, OpinionFullText, XGRQ, JSID, InfoPublDate, AuditReportsType, InsertTime) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_BalanceSheetAll 
(ID, InfoPublDate, InfoSource, BulletinType, CompanyCode, EndDate, IfAdjusted, IfMerged, AccountingStandards, EnterpriseType, CashEquivalents, ClientDeposit, TradingAssets, BillReceivable, DividendReceivable, InterestReceivable, AccountReceivable, OtherReceivable, AdvancePayment, Inventories, BearerBiologicalAssets, DeferredExpense, NonCurrentAssetIn1Year, OtherCurrentAssets, CAExceptionalItems, CAAdjustmentItems, TotalCurrentAssets, HoldForSaleAssets, HoldToMaturityInvestments, InvestmentProperty, LongtermEquityInvest, LongtermReceivableAccount, FixedAssets, ConstructionMaterials, ConstruInProcess, FixedAssetsLiquidation, BiologicalAssets, OilGasAssets, IntangibleAssets, SeatCosts, DevelopmentExpenditure, GoodWill, LongDeferredExpense, DeferredTaxAssets, OtherNonCurrentAssets, NCAExceptionalItems, NCAAdjustmentItems, TotalNonCurrentAssets, LoanAndAccountReceivables, SettlementProvi, ClientProvi, DepositInInterbank, RMetal, LendCapital, DerivativeAssets, BoughtSellbackAssets, LoanAndAdvance, InsuranceReceivables, ReceivableSubrogationFee, ReinsuranceReceivables, ReceivableUnearnedR, ReceivableClaimsR, ReceivableLifeR, ReceivableLTHealthR, InsurerImpawnLoan, FixedDeposit, RefundableDeposit, RefundableCapitalDeposit, IndependenceAccountAssets, OtherAssets, AExceptionalItems, AAdjustmentItems, TotalAssets, ShortTermLoan, ImpawnedLoan, TradingLiability, NotesPayable, AccountsPayable, STBondsPayable, AdvanceReceipts, SalariesPayable, DividendPayable, TaxsPayable, InterestPayable, OtherPayable, AccruedExpense, DeferredProceeds, NonCurrentLiabilityIn1Year, OtherCurrentLiability, CLExceptionalItems, CLAdjustmentItems, TotalCurrentLiability, LongtermLoan, BondsPayable, LongtermAccountPayable, SpecificAccountPayable, EstimateLiability, DeferredTaxLiability, OtherNonCurrentLiability, NCLExceptionalItems, NCLAdjustmentItems, TotalNonCurrentLiability, BorrowingFromCentralBank, DepositOfInterbank, BorrowingCapital, DerivativeLiability, SoldBuybackSecuProceeds, Deposit, ProxySecuProceeds, SubIssueSecuProceeds, DepositsReceived, AdvanceInsurance, CommissionPayable, ReinsurancePayables, CompensationPayable, PolicyDividendPayable, InsurerDepositInvestment, UnearnedPremiumReserve, OutstandingClaimReserve, LifeInsuranceReserve, LTHealthInsuranceLR, IndependenceLiability, OtherLiability, LExceptionalItems, LAdjustmentItems, TotalLiability, PaidInCapital, CapitalReserveFund, SurplusReserveFund, RetainedProfit, TreasuryStock, OrdinaryRiskReserveFund, ForeignCurrencyReportConvDiff, UncertainedInvestmentLoss, OtherReserves, SpecificReserves, SEExceptionalItems, SEAdjustmentItems, SEWithoutMI, MinorityInterests, OtherItemsEffectingSE, TotalShareholderEquity, LEExceptionalItems, LEAdjustmentItems, TotalLiabilityAndEquity, SpecialFieldRemark, UpdateTime, JSID, IfComplete, LPreferStock, LPerpetualDebt, OtherEquityinstruments, EPreferStock, EPerpetualDebt, OtherCompositeIncome, HoldAndFSAssets, HoldAndFSLi, LongSalariesPay, LongDeferIncome, BillAccReceivable, ContractualAssets, DebtInvestment, OthDebtInvestment, OthEquityInstrument, OthNonCurFinAssets, NotAccountsPayable, ContractLiability, TradeRiskRSRVFd, OtherReceivableED, OtherPayableED, ReceivablesFin, Financing, FinLeaseReceivable, ResReiReceContracts, UsufructAssets, AbsInterDeposits, InsContractReserve, LeaseLiabilities, FinLeasesPayable, TotalFixedAsset, TConstruInProcess, DepositInAssociate, DebtAssets, DebitofAssociate, InfoSourceCode, InsertTime, Cash, DepositInCentralBank, AmongTradingAssets, AmongFinAetAtFValTPL, Receivables, CashDepositReceive, PledgDepositReceive, SettlementReceive, RiskOfLossReceive, FeeCommissionReceive, AmongDebtInvestment, AmongFinAetAtAmorCost, AmongOthDebtInvest, AmongFinAetAtFValTOCI, AmongOthEquInstrument, AmongEquInsAtFValTOCI, FutureMemberInvestment, FinancialInvestment, ShortTermBondPay, AmongTradingLiability, AmongFinLiaAtFValTPL, Payables, CashDepositPay, PledgDepositPay, FutureProtectFundPay, GuarantCompensateRSRV, GuaranteeReserve, FutureRiskReserve, LTInsContractReserve, LTAccountPayableTotal, AgencyBusAssets, FinAssetsAtFValTOCI, SubLoan, PubWBiologicalAssets, AgencyBusLiability, SECParentCompanyOwners, TSEExceptionalItems) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_Buyback 
(ID, CompanyCode, FirstPublDate, InfoSource, ShareType, AdvanceDate, MeetPassDate, WriteOffPublDate, ContractDate, Seller, BuybackSum, Percentage, PricingStatement, BuybackPrice, BuybackMoney, StartDate, EndDate, PayMode, ChangeDate, PayDate, ChangeRegDate, XGRQ, JSID, VolumeFloor, VolumeCeiling, PriceFloor, PriceCeiling, ValueFloor, ValueCeiling, MaturityDesc, EventProcedure, EventProceDesc, BuybackModeCode, BuybackModeDesc, FundsSourceDesc, PurposeDesc, InsertTime, BuybackPurpose, CurrencyUnit, OverruledDate) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_BuybackAttach 
(ID, BuybackID, InfoPublDate, EffectiveDate, CurrencyUnit, BuybackSum, Percentage, CumulativeSum, CumulativeSumToTS, HighPrice, LowPrice, BuybackFunds, CumulativeValueSum, UpdateTime, JSID, InsertTime) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_COConcept 
(ID, InnerCode, ConceptCode, InDate, OutDate, IndiState, Remark, InfoPublDate, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_CapitalInvest 
(ID, CompanyCode, InitialInfoPunlDate, InfoPublDate, InfoSource, RaisingMethod, InvestProject, ProjectStatement, PlannedSum, ActualInvestEndDate, ActualSum, Industry, InvestField, ProceedingStatement, IfSwitched, ProjectSwitchedTo, SumSwitched, XGRQ, JSID, InnerCode, PurchaseType, BookValue, AppraisalValue, PurchasePrice, EquityRatio, Transferor, Relationship, InvolvedStock, TransferorNature, TargetName, TargetNature, InsertTime) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_CashFlowStatementAll 
(ID, InfoPublDate, InfoSource, BulletinType, CompanyCode, EndDate, IfAdjusted, IfMerged, AccountingStandards, EnterpriseType, GoodsSaleServiceRenderCash, TaxLevyRefund, NetDepositIncrease, NetBorrowingFromCentralBank, NetBorrowingFromFinanceCo, DrawBackLoansCanceled, InterestAndCommissionCashIn, NetDealTradingAssets, NetBuyBack, NetOriginalInsuranceCash, NetReinsuranceCash, NetInsurerDepositInvestment, OtherCashInRelatedOperate, SpecialItemsOCIF, AdjustmentItemsOCIF, SubtotalOperateCashInflow, GoodsServicesCashPaid, StaffBehalfPaid, AllTaxesPaid, NetLoanAndAdvanceIncrease, NetDepositInCBAndIB, NetLendCapital, CommissionCashPaid, OriginalCompensationPaid, NetCashForReinsurance, PolicyDividendCashPaid, OtherOperateCashPaid, SpecialItemsOCOF, AdjustmentItemsOCOF, SubtotalOperateCashOutflow, AdjustmentItemsNOCF, NetOperateCashFlow, InvestWithdrawalCash, Investproceeds, FixIntanOtherAssetDispoCash, NetCashDealSubCompany, OtherCashFromInvestAct, SpecialItemsICIF, AdjustmentItemsICIF, SubtotalInvestCashInflow, FixIntanOtherAssetAcquiCash, InvestCashPaid, NetCashFromSubCompany, ImpawnedLoanNetIncrease, OtherCashToInvestAct, SpecialItemsICOF, AdjustmentItemsICOF, SubtotalInvestCashOutflow, AdjustmentItemsNICF, NetInvestCashFlow, CashFromInvest, CashFromMinoSInvestSub, CashFromBondsIssue, CashFromBorrowing, OtherFinanceActCash, SpecialItemsFCIF, AdjustmentItemsFCIF, SubtotalFinanceCashInflow, BorrowingRepayment, DividendInterestPayment, ProceedsFromSubToMinoS, OtherFinanceActPayment, SpecialItemsFCOF, AdjustmentItemsFCOF, SubtotalFinanceCashOutflow, AdjustmentItemsNFCF, NetFinanceCashFlow, ExchanRateChangeEffect, OtherItemsEffectingCE, AdjustmentItemsCE, CashEquivalentIncrease, BeginPeriodCash, OtherItemsEffectingCEI, AdjustmentItemsCEI, EndPeriodCashEquivalent, NetProfit, MinorityProfit, AssetsDepreciationReserves, FixedAssetDepreciation, IntangibleAssetAmortization, DeferredExpenseAmort, DeferredExpenseDecreased, AccruedExpenseAdded, FixIntanOtherAssetDispoLoss, FixedAssetScrapLoss, LossFromFairValueChanges, FinancialExpense, InvestLoss, DeferedTaxAssetDecrease, DeferedTaxLiabilityIncrease, InventoryDecrease, OperateReceivableDecrease, OperatePayableIncrease, Others, SpecialItemsNOCF1, AdjustmentItemsNOCF1, NetOperateCashFlowNotes, ContrastAdjutmentNOCF, DebtToCaptical, CBsExpiringWithin1Y, FixedAssetsFinanceLeases, CashAtEndOfYear, CashAtBeginningOfYear, CashEquivalentsAtEndOfYear, CashEquivalentsAtBeginning, SpecialItemsC, AdjustmentItemsC, NetIncrInCashAndEquivalents, ContrastAdjutmentNC, SpecialFieldRemark, UpdateTime, JSID, IfComplete, NetIncBorFunds, NetCashRecInVTS, NetCashRecAgeUTS, NetIncFinAssTraPurp, NetIncCapResBusOper, NetIncCapResBusInv, CashRecIssOthEquIns, NetBuyBackFin, InterestExpense, IncResFunding, IncSpeReserves, CreditImpairmentL, DefProceedsAmo, IncEstLiability, NetDecFinancialAsset, NetCashPaidInVTS, UsufructAssetsDA, InfoSourceCode, InsertTime, NetDecLoanAndAdvance, NetDecreaseInCBAndIB, NetDecFundLending, NetDecCapResBusOper, NetDecFinAssTraPurp, NetIncFinLiaTraPurp, BFLAFValOnPLChange, NetDecBorrowFromCB, NetDecBorFromFinanceCo, NetDecInsurDPSTInvest, NetDecBorrowingCapital, NetDecOfBuyBack, NetCashPayAgeUTS, NetDecDealTradeAssets, NetDecFinLiaTraPurp, OpeAndAdmExpForCash, NetIncFinancialAsset, NetDecBuyBackFin, NPParentCompanyOwners, ProductBioAssetsDep, InterestIncome, LeaseLiaIntExp, BondIssueExpense, ExchangeLoss, DeferredTaxCredit, SharePayment, DecreaseTradeAssets, DecAvailableSaleAssets, DecreaseLoan, InvestPropertyDA) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ConceptList 
(ID, ClassCode, ClassName, SubclassCode, SubclassName, ConceptCode, ConceptName, BeginDate, EndDate, ConceptState, Remark, InfoPublDate, UpdateTime, JSID, ConceptEngName) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_Credit 
(ID, CompanyCode, InitialInfoPublDate, InfoPublDate, InfoSource, AnnouncementType, DisclosureMethod, EventContent, ActionDesc, NewestAdvance, EventSubject, EventProcedure, ActionWays, CurrencyUnit, SubjectName, SubjectCode, SubjectAssociation, ObjectName, ObjectCode, ObjectAssociation, AgreementDate, IfEnded, Note, LoanCondition, Borrower, BorrowerAssociation, MortgageAsset, Lender, LenderAssociation, Guarantor, GuarantorAssociation, GuarantorMortgageAsset, FirstLoanSum, LatestLoanSum, LatestRepaymentSum, AccumulatedRepaymentSum, YearRateStat, YearRate, LoanTerm, RenewalTerm, LoanBeginDate, LoanEndDate, LoanGuaranteeTerm, LoanRenewalGuaranteeTerm, LoanGuaranteeBeginDate, LoanGuaranteeEndDate, LatestRepaymentDate, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_Dividend 
(ID, InnerCode, EndDate, IfDividend, AdvanceDate, SMDeciPublDate, EPS, BonusShareRatio, TranAddShareRaio, PriceUnit, CashDiviRMB, ActualCashDiviRMB, CashDiviFC, ActualCashDiviFC, RightRegDate, ExDiviDate, BonusShareListDate, ToAccountDate, FinalTradingDay, DiviBase, SharesAfterDivi, DiviObject, TotalCashDiviComRMB, TotalCashDiviComFC, CashDiviAShare, CashDiviBShareRMB, CashDiviBShareFC, DiviStartDate, IFSchemeChange, ChangeStatement, ChangeType, IfDiviBeforeChange, BonusShareRatioBeforeChange, TranAddShareRatioBeforeChange, CashDiviBeforeChangeRMB, CashDiviBeforeChangeFC, DiviBaseBeforeChange, Notes, UndistributeStatement, DistributeTimes, CeilingNext, FloorNext, Ceiling, Floor, MainForm, CashDiviCeiling, CashDiviFloor, XGRQ, JSID, DiviEndDate, DividendImplementDate, EventProcedure, EventProcedureDesc, BonusSHRatioAdjusted, TranAddRatioAdjusted, CashDiviRMBAdjusted, DiviObjectNew, BonusShareArrivalDate, SchemeType, ExDiviRefPrice, DiviIntentPublDate, DividendBaseDate, ProposalSN, LatestInfoPublDate, SchemeStatement) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ESOP 
(ID, InnerCode, CompanyCode, IniInfoPublDate, DMAnnounceDate, SMAnnounceDate, Process, SerialNumber, IfPeriod, Period, InitialImpleDay, ShareSource, ShareCelling, ShareFloor, FundCelling, FundFloor, Duration, LockDuration, ReleaseDuration, FundSource, Participant, Management, ManageInsitute, PlanName, UpdateTime, JSID, PeriodSituation, PlanRatio, StockPrice, PartiAmount, ManagementPartiAmount, ManagementShares, ManagementRatio, EmployeePartiAmount, EmployeeShares, EmployeeRatio, ImpleEndDate, LockStartDate, Statement) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ESOPSummary 
(ID, InnerCode, CompanyCode, IniInfoPublDate, DMAnnounceDate, SMAnnounceDate, Process, SerialNumber, IfPeriod, ShareCelling, ShareFloor, FundCelling, FundFloor, Statement, UpdateTime, JSID, PeriodSituation) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_EntrustInv 
(ID, CompanyCode, InitialInfoPublDate, InfoPublDate, InfoSource, AnnouncementType, DisclosureMethod, EventContent, ActionDesc, NewestAdvance, EventSubject, EventProcedure, ActionWays, CurrencyUnit, SubjectName, SubjectCode, SubjectAssociation, ObjectName, ObjectCode, ObjectAssociation, nan, AgreementDate, IfEnded, Note, EntrustFinanceSum, EntrustFinanceTerm, EntrustFinanceBeginDate, EntrustFinanceEndDate, PromisedIncome, ActualIncome, XGRQ) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_IncomeStatementAll 
(ID, InfoPublDate, InfoSource, BulletinType, CompanyCode, EndDate, IfAdjusted, IfMerged, AccountingStandards, EnterpriseType, TotalOperatingRevenue, OperatingRevenue, NetInterestIncome, InterestIncome, InterestExpense, NetCommissionIncome, CommissionIncome, CommissionExpense, NetProxySecuIncome, NetSubIssueSecuIncome, NetTrustIncome, PremiumsEarned, PremiumsIncome, ReinsuranceIncome, Reinsurance, UnearnedPremiumReserve, OtherOperatingRevenue, SpecialItemsOR, AdjustmentItemsOR, TotalOperatingCost, OperatingPayout, RefundedPremiums, CompensationExpense, AmortizationExpense, PremiumReserve, AmortizationPremiumReserve, PolicyDividendPayout, ReinsuranceCost, OperatingAndAdminExpense, AmortizationReinsuranceCost, InsuranceCommissionExpense, OtherOperatingCost, OperatingCost, OperatingTaxSurcharges, OperatingExpense, AdministrationExpense, FinancialExpense, AssetImpairmentLoss, SpecialItemsTOC, AdjustmentItemsTOC, OtherNetRevenue, FairValueChangeIncome, InvestIncome, InvestIncomeAssociates, ExchangeIncome, OtherItemsEffectingOP, AdjustedItemsEffectingOP, OperatingProfit, NonoperatingIncome, NonoperatingExpense, NonCurrentAssetssDealLoss, OtherItemsEffectingTP, AdjustedItemsEffectingTP, TotalProfit, IncomeTaxCost, UncertainedInvestmentLosses, OtherItemsEffectingNP, AdjustedItemsEffectingNP, NetProfit, NPParentCompanyOwners, MinorityProfit, OtherItemsEffectingNPP, AdjustedItemsEffectingNPP, OtherCompositeIncome, AdjustedItemsEffectingCI, TotalCompositeIncome, CIParentCompanyOwners, CIMinorityOwners, AdjustedItemsEffectingPCI, BasicEPS, DilutedEPS, SpecialFieldRemark, UpdateTime, JSID, IfComplete, OCIParentCompanyOwners, OCINotInIncomeStatement, OCIReMearsure, OCIEquityNotInIS, OCIInIncomeStatement, OCIEquityInIS, OCIFairValue, OCIToMaturityFA, OCICFLoss, OCIForeignCurrencyFSA, OCIOthers, OCIMinorityOwners, OtherRevenue, AssetDealIncome, OperSustCateg, OperSustNetP, DisconOperNetP, OwnershipCateg, PreInsurRSRV, NetClaimIncurred, NetPremiumReserve, AmortisedcostIncome, InfoSourceCode, InsertTime, SalesRevenue, OtherOperatingIncome, GuaranteeIncome, BrokerageIncome, InvestBankIncome, AssetManageIncome, FundManageIncome, InvestConsultIncome, RiskManageIncome, InvestManageIncome, OtherAgencyIncome, BrokerageExpense, InvestBankExpense, AssetManageExpense, FundManageExpense, InvestConsultExpense, RiskManageExpense, InvestManageExpense, OtherAgencyExpense, NetFundMgtIncome, ExtractFutureRisk, WithdrawGuaranteeReser, GuarantCompRSRV, SalesCost, OtherOperationalCost, TotalAdminExpense, ExplorationCost, CreditImpairmentP, AssetImpairmentLossP, NPCParentCompanyOwners, NPOtherEqinstruments, OtherItemsEffectingCI, CICParentCompanyOwners, CIOtherEqinstruments, OthDebtInvesChange, InterestIncomeFin, CreditImpairmentL, NetOpenHedgeIncome, OthEquFVChange, FinAssetROtherCI, OtherDebtInvestCIP, RAndD, InterestFinExp, CorporateCRChange) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_IndFinIndicators 
(ID, IndustryNum, IndustryName, Classification, IndustryCode, Standard, StatType, SectorCode, InfoPublDate, EndDate, DataMark, ListedSecuNum, IndOperatingRevenueTTM, IndOperatingRevenue, IndOperatingCost, IndOperatingProfitTTM, IndOperatingProfit, IndNetProfitTTM, IndNetProfit, IndNPCOwnersTTM, IndNPParentComOwners, IndNetAssets, IndTotalAssets, IndTotalShares, EPSAvg, ROEAvg, ROE, ROETTM, WROECut, ROECut, ROAAvg, DilutedROA, ROATTM, GrossIncomeRatio, GrossIncomeRatioTTM, NetProfitRatio, NetProfitRatioTTM, NetProfitRatioCut, FinExpenseRateTTM, OperatingExpenseRate, OperatExpenseRateTTM, PeriodCostsRate, TOperatingCostToTOR, ROIC, CurrentRatio, QuickRatio, InterestCover, NOCFInterestCover, NPParentCompanyYOY, GrossProfitYOY, InventoryTRate, InventoryTDays, ARTRate, ARTDays, ReceivableTRate, TotalAssetTRate, NetOperCFToToOperReve, DebtAssetsRatio, NetTangibleAssetsTA, OutInvestOwnersEquity, AdvanceReceToTOR, AccountReceToTOR, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_IndexBasicInfo 
(ID, IndexCode, IndustryStandard, IndustryType, PubOrgName, CreatIndexOrgName, PubDate, BaseDate, BasePoint, WAMethod, IndexType, PubIndexType, IndexSeries, IndexPriceType, IndexDesignType, Relationship, RelaMainIndexCode, RelaMainCode, ComponentType, SecuMarket, ComponentSum, ComponentAdPeriod, CurrencyCode, IndexAbstract, IndexRemark, EndDate, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_IndexComponent 
(ID, IndexInnerCode, SecuInnerCode, InDate, OutDate, Flag, XGRQ, JSID, SecuMarket) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_IndustryValuation 
(PE_LYR, PB_LF, DividendRatio, PCF_TTM, PCF_LYR, PS_TTM, PS_LYR, InsertTime, UpdateTime, JSID, IndustryName, Classification, ListedSecuNum) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_InstiArchive 
(ID, CompanyCode, ParentCompany, ListedCode, InvestAdvisorName, TrusteeName, ChiName, AbbrChiName, NameChiSpelling, EngName, AbbrEngName, RegCapital, CurrencyUnit, EstablishmentDate, EconomicNature, CompanyNature, CompanyType, RegAddr, RegZip, RegCity, OfficeAddr, ContactAddr, ContactZip, ContactCity, Email, Website, LegalPersonRepr, GeneralManager, OtherManager, Contactman, Tel, Fax, BriefIntroText, BusinessMajor, Industry, StartDate, CloseDate, CloseReason, IfExisted, XGRQ, JSID, OrganizationCode, CompanyCval, CreditCode, RegArea, RegOrg, RegStatus, ID, CompanyCode, ParentCompany, ListedCode, InvestAdvisorName, TrusteeName, ChiName, AbbrChiName, NameChiSpelling, EngName, AbbrEngName, RegCapital, CurrencyUnit, EstablishmentDate, EconomicNature, CompanyNature, CompanyType, RegAddr, RegZip, RegCity, OfficeAddr, ContactAddr, ContactZip, ContactCity, Email, Website, LegalPersonRepr, GeneralManager, OtherManager, Contactman, Tel, Fax, BriefIntroText, BusinessMajor, Industry, StartDate, CloseDate, CloseReason, IfExisted, XGRQ, JSID, OrganizationCode, CompanyCval, CreditCode, RegArea, RegOrg, RegStatus) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_IntAssetsDetail 
(ID, InnerCode, CompanyCode, InfoPublDate, InfoSourceCode, EndDate, IfMerged, IfAdjusted, ExpensedRDInput, CapitalizedRDInput, TotalRDInput, RDInputRatio, CapitalizedRDInputR, RDStaffNum, RDStaffNumRatio, InsertTime, UpdateTime, JSID, CoreTechnicalStaffNum, CoreTechnicalStaffR, CoreTechnologyOutput, CoreTechnologyOutputR) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_InvestorDetail 
(ID, RID, Participant, ParticipantID, PersonalName, PersonalID, PostName, InsertTime, UpdateTime, JSID, SerialNumber) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_InvestorRa 
(ID, InfoPublDate, InnerCode, Nbcode, ReceptionDate, ReceptionDaTime, SerialNb, ActivitiesCate, Participant, Place, ListingCreper, TmainContent, ArticleFile, FileType, InfoTitle, LinkAddress, UpdateTime, JSID, ReceptionDateE) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_LegalDistribution 
(ID, InnerCode, InfoPublDate, InfoSource, DistributionSum, DistributionReason, SerialNum, AquirerName, AquirerCharacter, SecuCoBelongedCode, SecuCoBelonged, SecuCode, AquiredSum, OwnedPeriod, DistributeNature, FloatDate, Notes, XGRQ, JSID, IssuePrice, ValidApplyVol, RefundAmount, InitialInfoPublDate, SecuAccountNumber, SupplementAmount, RestrictedSum, NonRestrictedSum, InvestorName, InvestorType, InvestorCode, InsertTime, CoreStaffsStraSHVal, SponsorStraSharesHVal, OtherStraSHVol, OtherStraSHVal, OtherStraSHRat, BidderCode, AquirerAmount, StandardInvestorName, StandardAquirerName, AquirerType, ClassofInvestor) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_MainOperIncome 
(ID, CompanyCode, EndDate, DateType, InfoSource, IfMerged, IfAdjusted, Classification, SN, Project, Industry, RegionAndBusiness, MainOperIncome, MainOperCost, MainOperProfit, MainOperIncomeFormerYear, MainOperCostFormerYear, MainOperProfitFormerYear, MainIncomeGrowRateYOY, MainICostGrowRateYOY, MainProfitGrowRateYOY, XGRQ, JSID, GrossProfit, GrossProfitYOY, InsertTime, InfoPublDate, InfoSourceCode, CurrencyUnit, Level, ParentName, GrossProfitFormerYear, GrossProfitIncrease) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_MainSHListNew 
(ID, CompanyCode, EndDate, InfoPublDate, InfoSource, InfoTypeCode, SHNo, SHSerial, SHList, SHKind, SHTypeCode, SHType, SecuCoBelongedCode, SecuCoBelongedName, SecuCode, SecuAbbr, HoldSum, PCTOfTotalShares, RestrainedTShare, UnstintedTShare, HoldSumChange, HoldSumChangeRate, HoldAShareSum, PCTOfFloatShares, HoldBShareSum, HoldHShareSum, HoldOthterShareSum, ShareCharacterStatement, PledgeInvolvedSum, FreezeInvolvedSum, PFStatement, ConnectionRelation, ConnectionStatement, ActInConcertStatement, Notes, XGRQ, JSID, SecuInnerCode, SHKindCode, GDID, SHAttribute, RestrainedAShare, UnstintedAShare, HoldShareASum, RestrainedShareA, UnstintedShareA, HoldShareBSum, RestrainedShareB, UnstintedShareB, HoldShareCSum, HoldShareDSum, HoldOtherComShareSum, InsertTime, HoldChangeType, PrefShareWithVotRight, VotingRightsVol, VotingRightsRatio, SpecialVotingRightsVol, PCTOfNRShares, RefinanceLoanShare) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_MajorContract 
(ID, CompanyCode, InitialInfoPublDate, InfoPublDate, InfoSource, BulletinType, EventContent, ActionDesc, NewestAdvance, EventSubject, EventProcedure, ActionWays, CurrencyUnit, SubjectName, SubjectCode, SubjectAssociation, ObjectName, ObjectCode, ObjectAssociation, AgreementDate, ContractObject, ContractWay, AcceptanceDate, AmountInvolved, ContractBeginDate, ContractEndDate, ContractPeriod, ContractEffect, RemarkDesc, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_Mshareholder 
(ID, CompanyCode, InfoPublDate, InfoSource, MSHName, MSHPercentage, MSHNumber, GetMethod, LegalRepr, RegCapital, MainBusiness, EconomicNature, BackgroundIntr, IfExisted, XGRQ, JSID, BulletinType, NationalityDesc, PermanentResidency, StructureChart, FileType, EndDate, SHAttribute, CurrencyUnit, GDID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_NationalStockHoldSt 
(ID, InnerCode, CompanyCode, EndDate, SHID, SHName, HoldAShareSum, RestrainedAShare, UnstintedAShare, PCTOfTotalShares, PCTOfFloatShares, HoldASumChange, HoldASumChangeRate, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_OperatingStatus 
(ID, CompanyCode, EndDate, InfoSource, OperatingStatement, XGRQ, JSID, InfoPublDate) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_Regroup 
(CompanyCode, InitialInfoPublDate, InfoPublDate, InfoSource, AnnouncementType, DisclosureMethod, EventContent, ActionDesc, NewestAdvance, EventSubject, EventProcedure, ActionWays, CurrencyUnit, SubjectName, SubjectCode, SubjectAssociation, ObjectCode, ObjectAssociation, AgreementDate, IfEnded, Note, EventType, AssetBookValue, AppraisalValue, SaleProceeds, TransferIncome, BookValueOutAsset, AppraisalValueOutAsset, RepalcementPriceAssetOut, BookValueAssetIn, AppraisalValueAssetIn, RepalcementPriceAssetIn, DebtRearrangementSum, EventCode, SerialNumber, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_RewardStat 
(ID, CompanyCode, InfoPublDate, InfoSource, EndDate, TotalYearPay, NumPayManagers, High3Directors, High3Managers, TotalIndeSupeYearPay, Statement, XGRQ, JSID, TotalIndeSubsidy) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_SHNumber 
(ID, CompanyCode, InfoPublDate, InfoSource, EndDate, SHNum, AverageHoldSum, ASHNum, AAverageHoldSum, BSHNum, BAverageHoldSum, HSHNum, StaffSHNum, XGRQ, JSID, HoldProportionPAccount, ProportionChange, AvgHoldSumGRQuarter, ProportionGRQuarter, AvgHoldSumGRHalfAYear, ProportionGRHalfAYear, AHoldProportionPAccount, AProportionChange, AAvgHoldSumGRQuarter, AProportionGRQuarter, AAvgHoldSumGRHalfAYear, AProportionGRHalfAYear, AFAverageHoldSum, AFHoldProportionPAccount, AFProportionChange, AFAvgHoldSumGRQuarter, AFProportionGRQuarter, AFAvgHoldSumGRHalfAYear, AFProportionGRHalfAYear, BHoldProportionPAccount, BProportionChange, BAvgHoldSumGRQuarter, BProportionGRQuarter, BAvgHoldSumGRHalfAYear, BProportionGRHalfAYear, HHoldProportionPAccount, HProportionChange, HAvgHoldSumGRQuarter, HProportionGRQuarter, HAvgHoldSumGRHalfAYear, HProportionGRHalfAYear, AFHoldPropTA, CDRSHNum, CDRAverageHoldSum, CDRHoldPropPAccount, CDRProportionChange, CDRAvgHoldSumGRQtr, CDRPropGRQuarter, CDRAvgHoldSumGRHalfAY, CDRPropGRHalfAYear, CDRFAverageHoldSum, CDRFHoldPropPAccount, CDRFProportionChange, CDRFAvgHoldSumGRQtr, CDRFPropGRQuarter, CDRFAvgHoldSumGRHalfAY, CDRFPropGRHalfAYear, NumApproxiMark) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_SHTypeClassifi 
(ID, SHID, SHCode, SHName, SHAttribute, Standard, FirstLvCode, SecondLvCode, ThirdLvCode, FourthLvCode, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_SMAttendInfo 
(ID, CompanyCode, InitialInfoPublDate, LatestInfoPublDate, MeetingDate, SHMeetingTime, SMRegDate, MeetingRegStartDate, MeetingRegEndDate, AnounceDate, ProposalContent, CancelDate, Address, IfEffected, SerialNumber, MeetingType, VotingMeans, Year, Series, NetVotingPlatform, NetVotingCode, VotingAbbr, NetVotingStartDate, NetVotingEndDate, Presider, PresiderOfficialPost, TestmonyLawOffice, LawOfficeCode, Lawyer, AttendanceType, AttendanceNumber, ASharesNumber, HSharesNumber, OtherSharesNumber, ShareANumber, ShareBNumber, ShareReprensented, ASharesReprensented, HSharesReprensented, OSharesReprensented, ShareAReprensented, ShareBReprensented, RatioInTotalShare, ASharesRatio, HSharesRatio, OtherSharesRatio, ShareARatio, ShareBRatio, MSharesNumber, MShareReprensented, MSharesRatio, PSharesNumber, PSharesReprensented, PSharesRatio, InsertTime, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ShareFP 
(ID, CompanyCode, InfoPublDate, InfoSource, TypeSelect, FPSHName, ReceiverName, InvolvedSum, PCTOfPledger, PCTOfTotalShares, FPReason, StartDate, EndDate, Statement, XGRQ, JSID, SHSN, SHAttribute, SHID, ReceiverAttribute, ReceiverID, EventCode, EventDate, UnstintedTShare, RestrainedTShare, InitialInfoPublDate, InitialPledgeSum, EstimateReleaseDate) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ShareFPSta 
(ID, FPCode, EndDate, InfoSource, Category, CompanyCode, FPSHName, AccuFPShares, AccuPCTOfPled, AccuProportion, UpdateTime, AccuProportionCalc, SHAttribute, SHID, JSID, AccuFPSharesCalc) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ShareStru 
(ID, CompanyCode, InfoSource, EndDate, NonListedShares, PromoterShares, StateShares, DLegalPersonShares, FLegalPersonShares, OtherPromoterShares, RaisedLPShares, NaturalPersonHoldLPShares, StaffShares, RightsIssueTransferred, PreferredAndOtherShares, PreferredShares, FloatShare, AFloats, AFloatListed, ManagementShares, StategicInvestorShares, CommonLPShares, MutualFundShares, AdditionalIssueUnlisted, RightsIssueUnlisted, Bshares, Hshares, Sshares, Nshares, OtherFloatShares, TotalShares, ChangeType, ChangeReason, XGRQ, JSID, SLegalPersonShares, RaisedSLPShares, OtherAFloatShares, RestrictedAFloatShares, RestrinctStaffShares, NonListedBShares, InfoPublDate, RestrictedShares, StateHolding, SLegalPersonHolding, OtherDCapitalHolding, DLegalPersonHolding, DNaturalPersonHolding, ForeignHolding, FLegalPersonHolding, FNaturalPersonHolding, OtherRestrictedShares, RestrictedBFloatShares, PerValue, Ashares, NonRestrictedShares, BsharesTotal, ListedBShares, NonListedRestrictedBShares, ForeignHoldingAshares, RestrictedAShares, OtherFNonListedShares, NonResiSharesJY, RestrictAShareP, SRUnlistedShare, NonResiBShares, GDRshares, ParValueCurrencyUnit, InsertTime, NonRestrictedHShares, RestrictedHShares, OUnListedShares, OtherNonListedShares, Dshares) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ShareTransfer 
(ID, CompanyCode, InfoPublDate, InfoSource, ContractSignDate, ApprovedDate, TranDate, TransfererName, TansfererEcoNature, TranShareType, SumBeforeTran, PCTBeforeTran, SumAfterTran, PCTAfterTran, ReceiverName, ReceiverEcoNature, SumAfterRece, PCTAfterRece, TranMode, InvolvedSum, PCTOfTansferer, PCTOfTotalShares, DealPrice, DealTurnover, ValidCondition, TranStatement, IfSuspended, SuspendedPublDate, XGRQ, JSID, SNBeforeTran, SNAfterTran, SNAfterRece, IfSPBlockTradeCode, IfSPBlockTrade, InnerCode, ResSumAfterTran, NonResSumAfterTran, ResSumAfterRece, NonResSumAfterRece, InitialInfoPublDate, TransfererAttribute, TransfererCode, ReceiverAttribute, ReceiverCode, InsertTime, SumBeforeRece, PCTBeforerRece, TranStartDate, SerialNumber) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_Staff 
(ID, CompanyCode, EndDate, InfoSource, MergeMark, ClassfiedMethod, TypeName, YoungestAge, OldestAge, EmployeeSum, RatioInSum, Statement, XGRQ, JSID, TypeCode, InfoPublDate) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_StockHoldingSt 
(ID, InnerCode, CompanyCode, EndDate, InfoSource, InstitutionsHoldings, FundsHoldings, SecuritiesCorpsHoldings, FinancingProductsHoldings, QFIIHoldings, InsuranceCorpsHoldings, SocialSecurityFundHold, EnterpriseAnnuitiesHold, TrustCompaniesHoldings, FinanceCompaniesHoldings, OtherInstitutionHoldings, InstitutionsHoldProp, FundsHoldProp, SecuritiesCorpsHoldProp, FinancingProductsHoldProp, QFIIHoldProp, InsuranceCorpsHoldProp, SocialSecuFundHoldProp, CorpAnnuitiesHoldProp, TrustCompaniesHoldProp, FinanceCompaniesHoldProp, OtherInstitutionHoldProp, InstitutionsHoldingsA, FundsHoldingsA, SecuritiesCorpsHoldingsA, FinanceProductsHoldingsA, QFIIHoldingsA, InsuranceCorpsHoldingsA, SocialSecurityFundHoldA, EnterpriseAnnuitiesHoldA, TrustCompaniesHoldingsA, FinanceCompHoldingsA, OtherInstiHoldingsA, InstitutionsHoldPropA, FundsHoldPropA, SecuritiesCorpsHoldPropA, FinanceProductsHoldPropA, QFIIHoldPropA, InsuranceCorpsHoldPropA, SocialSecuFundHoldPropA, CorpAnnuitiesHoldPropA, TrustCompaniesHoldPropA, FinanceCompHoldPropA, OtherInstiHoldPropA, InstitutionsHoldingsT, FundsHoldingsT, SecuritiesCorpsHoldingsT, FinanceProductsHoldingsT, QFIIHoldingsT, InsuranceCorpsHoldingsT, SocialSecurityFundHoldT, EnterpriseAnnuitiesHoldT, TrustCompaniesHoldingsT, FinanceCompHoldingsT, OtherInstiHoldingsT, InstitutionsHoldPropT, FundsHoldPropT, SecuritiesCorpsHoldPropT, FinanceProductsHoldPropT, QFIIHoldPropT, InsuranceCorpsHoldPropT, SocialSecuFundHoldPropT, CorpAnnuitiesHoldPropT, TrustCompaniesHoldPropT, FinanceCompHoldPropT, OtherInstiHoldPropT, Top10StockholdersAmount, Top10StockholdersProp, Top10NRStockholdersAmount, Top10NRHoldersAmountToNRS, Top10NRHoldersAmountToTS, NRAFromTop10NRHolders, NRAFromTop10ToNRA, UpdateTime, JSID, InstiHoldTNum, InstiHoldANum, InstiHoldNum, FundsHoldingsTNum, SecuCorpsHoldTNum, SecuCorpsHoldANum, SecuCorpsHoldNum, FinProductsHoldTNum, FinProductsHoldANum, FinProductsHoldNum, QFIIHoldTNumber, QFIIHoldANum, QFIIHoldingsNum, InsurCorpsHoldTNum, InsurCorpsHoldANum, InsurCorpsHoldNum, SocialSecuFundHoldTN, SocialSecuFundHoldAN, SocialSecuFundHoldN, EntAnnuitiesHoldTNum, EntAnnuitiesHoldANum, EntAnnuitiesHoldNum, TrustCoHoldTNum, TrustCoHoldANum, TrustCoHoldNum, FinanceCoHoldTNum, FinanceCoHoldANum, FinanceCoHoldNum, OtherInstiHoldTNum, OtherInstiHoldANum, OtherInstiHoldNum, InsertTime, StatDate, PrivFundHoldings, BankHoldings, ForeignInstHoldings, PrivFundHoldProp, BankHoldProp, ForeignInstHoldProp, PrivFundHoldNum, BankHoldNum, ForeignInstHoldNum, PrivFundHoldingsA, BankHoldingsA, ForeignInstHoldingsA, PrivFundHoldPropA, BankHoldPropA, ForeignInstHoldPropA, FundsHoldingsANum, PrivFundHoldANum, BankHoldANum, ForeignInstHoldANum, PrivFundHoldingsT, BankHoldingsT, ForeignInstHoldingsT, PrivFundHoldPropT, BankHoldPropT, ForeignInstHoldPropT, PrivFundHoldTNum, BankHoldTNum, ForeignInstHoldTNum) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_SuitArbitration 
(id, CompanyCode, InitialInfoPublDate, InfoPublDate, InfoSource, AnnouncementType, DisclosureMethod, EventContent, ActionDesc, NewestAdvance, EventSubject, EventProcedure, ActionWays, CurrencyUnit, SubjectName, SubjectCode, SubjectAssociation, ObjectName, ObjectCode, ObjectAssociation, AgreementDate, IfEnded, Note, FirstSuitSum, LatestSuitSum, Plaintiff, PlaintiffAssociation, Defendant, DefendantAssociation, JSRParty, JSRPartyAssociation, OtherParty, OtherPartyAssociation, SubjectMatterStat, SubjectMatter, EventSubjectRole, InquisitionInstitute, CaseStatus, FirstInstanceStatus, SecondInstanceStatus, SPPStatus, PropertyEnforcement, PropertyEnforced, PropertyBelonged, AdjudgementStatus, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_SuppCustDetail 
(ID, InfoPublDate, CompanyCode, InfoSource, InfoSourceCode, EndDate, RelationType, SerialNumber, RelatedPartyName, RelatedPartyCode, RelatedPartyAttribute, TargetName, TargetCode, TradingValue, Ratio, Remark, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_SuspendResumption 
(ID, InnerCode, InfoPublDate, InfoSource, SuspendDate, SuspendTime, SuspendReason, SuspendStatement, SuspendTerm, ResumptionDate, ResumptionTime, ResumptionStatement, UpdateTime, JSID, InsertTime, SuspendType) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_TransferPlan 
(ID, CompanyCode, InitialInfoPublDate, InfoPublDate, InfoSource, PromiseSubject, EventType, IfEffected, EventProcedure, SHSN, SHName, TransferPlanType, PromiseBeginDate, PromiseEndDate, PromiseStatment, IncreaseTime, IncreaseTerm, IncreasePriceStatement, IncreasePriceCeiling, IncreasePriceFloor, IncreaseSize, IncreaseShareCeiling, IncreaseShareFloor, IncreaseRatioCeiling, IncreaseRatioFloor, IncreaseFundCeiling, IncreaseFundFloor, NotReducePromise, TradeType, TradeTypeStatment, ReduceTime, ReduceTerm, ReducePriceStatement, ReducePriceCeiling, ReducePriceFloor, ReduceSize, ReduceShareCeiling, ReduceShareFloor, ReduceRatioCeiling, ReduceRatioFloor, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_ViolatiParty 
(ID, RID, EventCode, PartyName, PartyType, PartyCode, BeginDate, EndDate, ViolationClause, PenalOrg, PenalType, AmountInvolved, CurrencyCode, PenalStatement, UpdateTime, JSID, PenalOrgCode, RelataCompany, PenalTypeNew, ViolationStatement, InsertTime, AnnID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO LC_Warrant 
(ID, CompanyCode, InitialInfoPublDate, InfoPublDate, InfoSource, AnnouncementType, DisclosureMethod, EventContent, ActionDesc, NewestAdvance, EventSubject, EventProcedure, ActionWays, CurrencyUnit, SubjectName, SubjectCode, SubjectAssociation, ObjectName, ObjectCode, ObjectAssociation, AgreementDate, IfEnded, Note, GuaranteeReason, FirstGuaranteeSum, LatestGuaranteeSum, GuarantorCompany, GuarantorAssociation, GuaranteeAsset, SecuredParty, SecuredPartyAssociation, CounterGuarantor, CGuarantorAssociation, CGuaranteeAsset, LendBank, LendTerm, RenewalTerm, LendBeginDate, LendEndDate, GuaranteeTerm, RenewalGuaranteeTerm, GuaranteeBeginDate, GuaranteeEndDate, DischargeGuaranteeDate, DischargeGuaranteeWays, IfIllegality, IfOverdue, XGRQ, JSID, EventCode) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO MF_Dividend 
(ID, TransCode, InnerCode, InfoPublDate, InfoSource, DividendImplementDate, EndDate, ProfitDistDate, UnitProfit, UnitRetainedProfit, IfDistributed, DividendRatioBeforeTax, ActualRatioAfterTax, Dividendsum, ReDate, ExRightDate, ExRightDateEX, ExecuteDate, ExecuteDateEX, ReinvestDay, AccountDay, RedemptionDay, DistributableProfits, AllocationValue, SchemeModification, EventProcedureCode, EventProcedure, DistributedRange, UnitProfitYTD, DividendSumYTD, DividendTimesYTD, DiviSumSinceInception, DiviTimesSinceIncepion, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO MF_FundArchives 
(ID, InnerCode, TransCode, ApplyingCodeFront, ApplyingCodeBack, SecurityCode, SecuCode, MainCode, ExApplyingMarket, ExApplyingCode, ExApplyingAbbr, Type, FundNature, InvestmentType, InvestStyle, FundType, FundTypeCode, InvestOrientation, InvestTarget, InvestField, PerformanceBenchMark, RiskReturncharacter, ProfitDistributionRule, ExProfitDistri, OTCProfitDistri, BriefIntro, FloatType, FoundedSize, EstablishmentDate, EstablishmentDateII, ListedDate, Duration, StartDate, ExpireDate, LastOperationDate, StClearingDate, EnClearingDate, GuaranteedPeriod, CarryOverDate, CarryOverDateRemark, CarryOverType, AgrBenchmkRateOfShareA, AgrBenchmkRateOfShareANotes, ShareProperties, RegularShareConversionNotes, NonRegularShareConversionNotes, Manager, InvestAdvisorCode, TrusteeCode, Warrantor, RegInstCode, LowestSumSubscribing, LowestSumSubLL, LowestSumPurLL, LowestSumRedemption, LSFRDescription, LowestSumForHolding, LSFHDescription, LargeRedemptionRatio, PRconfirmationdate, DeliveryDays, CustodyMarket, IfInitiatingFund, IfPensionTarget, IfFOF, InsertTime, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO MF_FundProdName 
(ID, InnerCode, InfoPublDate, InfoSource, InfoType, DisclName, EffectiveDate, ExpiryDate, IfEffected, Remark, UpdateTime, JSID, ChiSpelling, TransCode, InsertTime) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO MF_InvestAdvisorOutline 
(ID, InvestAdvisorCode, InvestAdvisorName, InvestAdvisorAbbrName, LegalRepr, GeneralManager, EstablishmentDate, OrganizationForm, RegCapital, RegAddr, OfficeAddr, ZipCode, Email, ContactAddr, Tel, Fax, WebSite, LinkMan, Background, Region, XGRQ, JSID, ServiceLine, MaturityEndDate, TACode, CSRCCode) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO PS_EventStru 
(ID, EventName, EventCode, FEventCode, EventLevel, IfEffected, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO PS_NewsSecurity 
(ID, RID, InnerCode, CompanyCode, EventType, EventName, EventDate, EmotionDirection, EmotionImportance, InsertTime, UpdateTime, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO QT_DailyQuote 
(ID, InnerCode, TradingDay, PrevClosePrice, OpenPrice, HighPrice, LowPrice, ClosePrice, TurnoverVolume, TurnoverValue, TurnoverDeals, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO QT_StockPerformance 
(ID, InnerCode, TradingDay, PrevClosePrice, OpenPrice, HighPrice, LowPrice, ClosePrice, TurnoverVolume, TurnoverValue, ChangePCT, RangePCT, TurnoverRate, AvgPrice, Ifsuspend, TurnoverValueRW, TurnoverVolumeRW, ChangePCTRW, RangePCTRW, TurnoverRateRW, AvgPriceRW, HighPriceRW, LowPriceRW, HighestClosePriceRW, LowestClosePriceRW, TurnoverValuePerDayRW, TurnoverRatePerDayRW, TurnoverValueTW, TurnoverVolumeTW, ChangePCTTW, RangePCTTW, TurnoverRateTW, AvgPriceTW, HighPriceTW, LowPriceTW, HighestClosePriceTW, LowestClosePriceTW, TurnoverValuePerDayTW, TurnoverRatePerDayTW, TurnoverValueRM, TurnoverVolumeRM, ChangePCTRM, RangePCTRM, TurnoverRateRM, AvgPriceRM, HighPriceRM, LowPriceRM, HighestClosePriceRM, LowestClosePriceRM, TurnoverValuePerDayRM, TurnoverRatePerDayRM, TurnoverValueTM, TurnoverVolumeTM, ChangePCTTM, RangePCTTM, TurnoverRateTM, AvgPriceTM, HighPriceTM, LowPriceTM, HighestClosePriceTM, LowestClosePriceTM, TurnoverValuePerDayTM, TurnoverRatePerDayTM, TurnoverValueRMThree, TurnoverVolumeRMThree, ChangePCTRMThree, RangePCTRMThree, TurnoverRateRMThree, TurnoverValueRMSix, TurnoverVolumeRMSix, ChangePCTRMSix, RangePCTRMSix, TurnoverRateRMSix, TurnoverValueRY, TurnoverVolumeRY, ChangePCTRY, RangePCTRY, TurnoverRateRY, AvgPriceRY, HighPriceRY, LowPriceRY, HighestClosePriceRY, LowestClosePriceRY, TurnoverValuePDayRY, TurnoverRatePDayRY, TurnoverValueYTD, TurnoverVolumeYTD, ChangePCTYTD, RangePCTYTD, TurnoverRateYTD, AvgPriceYTD, HighPriceYTD, LowPriceYTD, HighestClosePriceYTD, LowestClosePriceYTD, TurnoverValuePerDayYTD, TurnoverRatePerDayYTD, HighAdjustedPrice, HighAdjustedPriceDate, LowAdjustedPrice, LowAdjustedPriceDate, BetaLargeCapIndex, BetaCompositeIndex, BetaSYWGIndustryIndex, BetaMidCapIndex, BetaWeekly, AdjustBetaWeekly, AlphaLargeCapIndex, AlphaCompositeIndex, AlphaSYWGIndustryIndex, AlphMidCapIndex, YearVolatilityByDay, YearVolatilityByWeek, YearSharpeRatio, MarketIndexRORArithAvg, MarketIndexRORGeomMean, TotalMV, NegotiableMV, UpdateTime, InsertTime, JSID, TurnoverRateFreeFloat, TurnoverRateFFTRW, TurnoverRatePDFFTRW, TurnoverRateFFTTW, TurnoverRatePDFFTTW, TurnoverRateFFTRM, TurnoverRatePDFFTRM, TurnoverRateFFTTM, TurnoverRatePDFFTTM, TurnoverRateFFTRMThree, TurnoverRateFFTRMSix, TurnoverRateFFTRY, TurnoverRatePDFFTRY, TurnoverRateFFTYTD, TurnoverRatePDFFTYTD) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO QT_TradingDayNew 
(ID, TradingDate, IfTradingDay, SecuMarket, IfWeekEnd, IfMonthEnd, IfQuarterEnd, IfYearEnd, XGRQ, JSID, ID, TradingDate, IfTradingDay, SecuMarket, IfWeekEnd, IfMonthEnd, IfQuarterEnd, IfYearEnd, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO SecuMain 
(ID, InnerCode, CompanyCode, SecuCode, ChiName, ChiNameAbbr, EngName, EngNameAbbr, SecuAbbr, ChiSpelling, ExtendedAbbr, ExtendedSpelling, SecuMarket, SecuCategory, ListedDate, ListedSector, ListedState, ISIN, XGRQ, JSID) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO US_CompanyInfo 
(ID, CompanyCode, EngName, EngNameAbbr, ChiName, PEOAddress, PEOCity, PEOState, PEOZip, PEOStatus, PEOTel, BusinessDcrp, UpdateTime, JSID, BriefIntroText, EstablishmentDate, CompanyType, BriefIntroTextEng, Fax, RegCountry, RegState, BusinessDcrpEng, IfHeadOffice, LinkAddress, CountryCode, EstablishmentDatePreci, InsertTime) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO US_DailyQuote 
(ID, TradingDay, InnerCode, Open, High, Low, Close, Volume, EPSTTM, MarketCap, ShareOST, UpdateTime, JSID, PrevClosePrice, ChangePCT, AvgPrice, TurnoverValue, ChangeOF) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO US_SecuMain 
(ID, InnerCode, SecuCode, SecuAbbr, ChiSpelling, SecuCategory, SecuMarket, ListedSector, ListedDate, ListedState, ISIN, CompanyCode, UpdateTime, JSID, DelistingDate, InsertTime, EngName, ChiName) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);


INSERT INTO _IndustryValuation 
(PE_TTM) 
VALUES 
(%s);

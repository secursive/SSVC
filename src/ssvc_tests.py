#!/usr/bin/env python
'''
file: ssvc_tests
author: secursive
reference: https://secursive.github.io/posts/1-Critical-Look-Stakeholder-Specific-Vulnerability-Categorization-SSVC.html
'''

import unittest
import itertools
import pprint
from ssvc import _app_cols, _dev_cols, _app_lookup, _dev_lookup, _df_applier, _df_developer, applier_tree, developer_tree

'''
Test class
'''
class SSVC_Tests(unittest.TestCase):
	_dict_all_cols = {
		'TechnicalImpact': ['partial', 'total'],
		'Utility': ['laborious', 'efficient', 'super effective'],
		'Exposure': ['small', 'controlled', 'unavoidable'],
		'MissionImpact': ['none', 'degraded', 'MEF crippled', 'MEF fail', 'mission fail'],
		'Exploitation': ['none', 'poc', 'active'],
		'SafetyImpact': ['none', 'minor', 'major', 'hazardous', 'catastrophic'],
		'Outcome': ['defer', 'scheduled', 'immediate', 'out-of-band']
	}
	_dict_all_cols_nums = {
		'TechnicalImpact': {
			'partial':1,
			'total':2
		},
		'Utility': {
			'laborious': 1,
			'efficient': 2,
			'super effective': 3
		},
		'Exposure': {
			'small': 1,
			'controlled': 2,
			'unavoidable': 3
		},
		'MissionImpact': {
			'none': 1,
			'degraded': 2,
			'MEF crippled': 3,
			'MEF fail': 4,
			'mission fail': 5
		},
		'Exploitation': {
			'none': 1,
			'poc': 2,
			'active': 3
		},
		'SafetyImpact': {
			'none': 1,
			'minor': 2,
			'major': 3,
			'hazardous': 4,
			'catastrophic': 5
		},
		'Outcome': {
			'defer': 1,
			'scheduled': 2,
			'out-of-band': 3,
			'immediate': 4
		}
	}
	def test_inner_merge(self):
		print('\n=== [ Inner Merge ] ===\n')
		merged_df = _df_applier.merge(_df_developer, how='inner', sort=True)
		print('Writing output file ../data/ssvc_1_inner_merge.csv')
		merged_df.to_csv('../data/ssvc_1_inner_merge.csv')
	def test_outer_merge(self):
		print('\n=== [ Outer Merge ] ===\n')
		merged_df = _df_applier.merge(_df_developer, how='outer', sort=True)
		print('Writing output file ../data/ssvc_1_outer_merge.csv')
		merged_df.to_csv('../data/ssvc_1_outer_merge.csv')
	def test_inner_merge_numbers(self):
		print('\n=== [ Inner Merge (Numerical)] ===\n')
		df_developer_num = _df_developer.replace(to_replace=self._dict_all_cols_nums)
		df_applier_num = _df_applier.replace(to_replace=self._dict_all_cols_nums)
		merged_df = df_applier_num.merge(df_developer_num, how='inner', sort=True)
		print('Writing output file ../data/ssvc_1_inner_merge_numbers.csv')
		merged_df.to_csv('../data/ssvc_1_inner_merge_numbers.csv')
	def test_outer_merge_numbers(self):
		print('\n=== [ Outer Merge (Numerical)] ===\n')
		df_developer_num = _df_developer.replace(to_replace=self._dict_all_cols_nums)
		df_applier_num = _df_applier.replace(to_replace=self._dict_all_cols_nums)
		merged_df = df_applier_num.merge(df_developer_num, how='outer', sort=True)
		print('Writing output file ../data/ssvc_1_outer_merge_numbers.csv')
		merged_df.to_csv('../data/ssvc_1_outer_merge_numbers.csv')
	def test_outcome_divergence(self):
		print('\n=== [ Outcome Divergence] ===\n')
		dict_all_cols = self._dict_all_cols
		dict_all_cols.pop('Outcome')
		dict_all_cols_keys = list(dict_all_cols.keys())
		dict_all_cols_values = list(dict_all_cols.values())
		combs_values = list(itertools.product(*dict_all_cols_values))
		combs_keys = dict_all_cols_keys
		div_diff = {0: 0, 1:0, 2:0, 3:0}
		div_sets = set() # set of (dev_outcome, app_outcome) sets
		div_max_examples = list()
		for c_v in combs_values:
			c_v = dict(zip(combs_keys, list(c_v)))
			exploitation = c_v['Exploitation']
			utility = c_v['Utility']
			technical_impact = c_v['TechnicalImpact']
			safety_impact = c_v['SafetyImpact']
			exposure = c_v['Exposure']
			mission_impact = c_v['MissionImpact']
			dev_item = developer_tree(exploitation=exploitation, utility=utility, technical_impact=technical_impact, safety_impact=safety_impact)
			app_item = applier_tree(exploitation=exploitation, exposure=exposure, mission_impact=mission_impact, safety_impact=safety_impact)
			dev_outcome = dev_item['Outcome']
			app_outcome = app_item['Outcome']
			outcome_dict = self._dict_all_cols_nums['Outcome']
			dev_outcome_number = outcome_dict[dev_outcome]
			app_outcome_number = outcome_dict[app_outcome]
			div_sets.add((dev_outcome, app_outcome))
			outcome_diff = abs(dev_outcome_number - app_outcome_number)
			div_diff[outcome_diff] = div_diff[outcome_diff] + 1
			if outcome_diff == max(div_diff.keys()):
				c_v_example = c_v
				c_v_example['DeveloperOutcome'] = dev_outcome
				c_v_example['ApplierOutcome'] = app_outcome
				div_max_examples.append(c_v_example)
		print('Writing output file ../data/ssvc_1_divergence.txt')
		with open('../data/ssvc_1_divergence.txt', 'w+') as f_div:
			f_div.write('Frequency of difference between Developer and Applier outcomes:\n')
			pprint.pprint(div_diff, stream=f_div)
			f_div.write('\nCombinations of unique (Developer Outcome, Applier Outcome) possible sets:\n')
			pprint.pprint(div_sets, stream=f_div)
			f_div.write('\nCombinations that lead to maximum possible difference between Developer and Applier Outcome:\n')
			pprint.pprint(div_max_examples, stream=f_div)

def main():
	print('\nTest Details: https://secursive.github.io/posts/1-Critical-Look-Stakeholder-Specific-Vulnerability-Categorization-SSVC.html')
	unittest.main()

if __name__ == '__main__':
	main()
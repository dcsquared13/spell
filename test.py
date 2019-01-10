from LCSMap import LCSMap

threshold = .5
t = LCSMap(threshold)
t.insert("Dan assigned role bigquery/viewer")
t.insert("Bill assigned role bigquery/viewer")
t.insert("Bill assigned role bigquery/admin")
t.insert("Justin assigned role project/owner")
t.insert("Bill deleted role test/role")

t.to_string()

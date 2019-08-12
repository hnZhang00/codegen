<template>
    <div class="page-table" >
        <div class="table-header">
            <div class="table-header-title">页面2</div>
        </div>
        <div class="table-content" v-loading="pageLoading">
            <el-table :data="tableList" border stripe style="width: 100%">
                <el-table-column prop="field_21" label="字段_21" width="150">
                    <template slot-scope="scope">
						{{ scope.field_21 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_22" label="字段_22" width="150">
                    <template slot-scope="scope">
						{{ scope.field_22 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_23" label="字段_23" width="150">
                    <template slot-scope="scope">
						{{ scope.field_23 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_24" label="字段_24" width="150">
                    <template slot-scope="scope">
						{{ scope.field_24 }}
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <div class="table-footer">
            <my-search-pagination
                :limit="data.limit"
                :totalCount="data.totalCount"
                :pageChange="handle().pageChange"
            ></my-search-pagination>
        </div>
    </div>
</template>

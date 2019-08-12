<template>
    <div class="page-table" >
        <div class="table-header">
            <div class="table-header-title">页面3</div>
        </div>
        <div class="table-content" v-loading="pageLoading">
            <el-table :data="tableList" border stripe style="width: 100%">
                <el-table-column prop="field_31" label="字段_31" width="150">
                    <template slot-scope="scope">
						{{ scope.field_31 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_32" label="字段_32" width="150">
                    <template slot-scope="scope">
						{{ scope.field_32 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_33" label="字段_33" width="150">
                    <template slot-scope="scope">
						{{ scope.field_33 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_34" label="字段_34" width="150">
                    <template slot-scope="scope">
						{{ scope.field_34 }}
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

<template>
    <div class="page-table" >
        <div class="table-header">
            <div class="table-header-title">页面1</div>
        </div>
        <div class="table-content" v-loading="pageLoading">
            <el-table :data="tableList" border stripe style="width: 100%">
                <el-table-column prop="field_11" label="字段_11" width="150">
                    <template slot-scope="scope">
						{{ scope.field_11 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_12" label="字段_12" width="150">
                    <template slot-scope="scope">
						{{ scope.field_12 | dateToTime }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_13" label="字段_13" width="150">
                    <template slot-scope="scope">
						{{ scope.field_13 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_14" label="字段_14" width="150">
                    <template slot-scope="scope">
						{{ scope.field_14 }}
                    </template>
                </el-table-column>
                <el-table-column prop="field_15" label="操作" width="150">
                    <template slot-scope="scope">
                        <span>
                            <el-button
                                @click="handle().detail(scope.row)"
                                type="text"
                                size="small"
                            >详情</el-button>
                            <el-button
                                @click="handle().detail(scope.row)"
                                type="text"
                                size="small"
                            >修改</el-button>
                            <el-button
                                @click="handle().detail(scope.row)"
                                type="text"
                                size="small"
                            >删除</el-button>
                        </span>
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
